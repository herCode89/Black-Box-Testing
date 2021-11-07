import sys
''' Assignment 2- Black Box Testing
    By: Frankie Herbert (CS-362)    '''
import unittest

from credit_card_validator import credit_card_validator


class TestSuite(unittest.TestCase):

    # Verifies if Visa with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_visa_1(self):
        num = "4113601923182357"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Visa with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_visa_2(self):
        num = "4079585412272062"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Visa with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_visa_3(self):
        num = "4051071863870110"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Visa with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_visa_4(self):
        num = "4291162103544563"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Visa with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_visa_5(self):
        num = "4378974285038156"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if MasterCard with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_6(self):
        num = "5574231856733536"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if MasterCard with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_7(self):
        num = "5372079057540208"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if MasterCard with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_8(self):
        num = '5372078305004470'
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if AE with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_AE_9(self):
        num = "370008240124128"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if AE with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_AE_10(self):
        num = "349936268704645"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_11(self):
        num = "5372071982684458"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_12(self):
        num = "5574725437427351"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_13(self):
        num = "5574841608436475"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Visa with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_visa_14(self):
        num = "4544876328526551"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_15(self):
        num = "5372070338676572"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Visa with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_visa_16(self):
        num = "464292181282163"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if AE with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_AE_17(self):
        num = "349183426759183"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if AE with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_AE_18(self):
        num = "364000000000000"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_19(self):
        num = "5372075726200711"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_20(self):
        num = "5372070536230073"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_21(self):
        num = "5372073180248714"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if AE with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_AE_22(self):
        num = "349948258388271"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if AE with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_AE_23(self):
        num = "370024386273850"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if AE with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_AE_24(self):
        num = "370036077427124"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if AE with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_AE_25(self):
        num = "370036404655702"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_26(self):
        num = "5574725737334638"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_27(self):
        num = "5372074154670487"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_28(self):
        num = "2576759183426759"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_29(self):
        num = "2720134267591834"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_30(self):
        num = "2601334267591834"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_31(self):
        num = "2221003919370588"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_32(self):
        num = "2221000634622624"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_33(self):
        num = "2720993577902852"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if AE with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_AE_34(self):
        num = "377160851739943"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if AE with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_AE_35(self):
        num = "347593847126253"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if AE with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_AE_36(self):
        num = "3542097486980704"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if AE with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_AE_37(self):
        num = "3536322585727386"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_38(self):
        num = "2576759183426759"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_39(self):
        num = "2221091834267591"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Master Cards with valid lengths and invalid check bits generated
    # Picked using Luhn Number Checksum
    def test_mastercard_40(self):
        num = "2301026759183420"
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Any card has valid lengths and invalid check bits generated
    # Picked using Wild Guessing
    def test_41(self):
        num = ""
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Any card has valid lengths and invalid check bits generated
    # Picked using Wild Guessing
    def test_42(self):
        num = ""
        self.assertFalse(credit_card_validator(num))
        pass

    # Verifies if Any card has valid lengths and invalid check bits generated
    # Picked using Wild Guessing
    def test_43(self):
        num = ""
        self.assertFalse(credit_card_validator(num))
        pass


if __name__ == '__main__':
    unittest.main()
