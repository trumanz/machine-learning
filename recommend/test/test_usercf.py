import unittest
from data import testdata
from usercf.usercf import UserCF
from evaluator import  evaluate

class TestUserCF(unittest.TestCase):
    
    def test_samll_data(self):
        print("\n")
        (train_data, test_data) = testdata.get_samll_test_data()
        test_user_view_data = testdata.tranform2UserView(test_data)
        user_cf = UserCF()
        user_cf.train_v2(train_data)
        users = set( [ k for k in test_user_view_data] )
        # pprint.pprint(users)
        recommendataion =  user_cf.recommend_multi_users(users, k=3, n=10)
        result = evaluate(test_user_view_data, recommendataion)
        print(result)
    def test_1m_data(self):
        print("\n")
        (train_data, test_data) = testdata.get_1m_data()
        user_cf = UserCF()
        user_cf.train_v2(train_data)
        users = set([k for k in test_user_view_data])
        # pprint.pprint(users)
        recommendataion = user_cf.recommend_multi_users(users, k=3, n=10)
        result = evaluate(test_user_view_data, recommendataion)
        print(result)
