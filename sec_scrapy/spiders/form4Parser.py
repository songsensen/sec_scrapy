from lxml import etree


class Issuer:
    def __init__(self,
                 issuer_cik,
                 issuer_name,
                 issuer_trading_symbol):
        self.issuer_cik = issuer_cik
        self.issuer_name = issuer_name
        self.issuer_trading_symbol = issuer_trading_symbol

    def __str__(self):
        issuer_str = f'issuer_cik: {self.issuer_cik}\n' \
                     f'issuer_name: {self.issuer_name}\n' \
                     f'issuer_trading_symbol: {self.issuer_trading_symbol}\n'
        return issuer_str


class ReportingOwnerId:
    def __init__(self,
                 rpt_owner_cik,
                 rpt_owner_name):
        self.rpt_owner_cik = rpt_owner_cik
        self.rpt_owner_name = rpt_owner_name

    def __str__(self):
        reporting_owner_id_str = f'rpt_owner_cik: {self.rpt_owner_cik}\n' \
                                 f'rpt_owner_name: {self.rpt_owner_name}\n'
        return reporting_owner_id_str


class ReportingOwnerAddress:
    def __init__(self,
                 rpt_owner_street1,
                 rpt_owner_street2,
                 rpt_owner_city,
                 rpt_owner_state,
                 rpt_owner_zip_code,
                 rpt_owner_state_description):
        self.rpt_owner_street1 = rpt_owner_street1
        self.rpt_owner_street2 = rpt_owner_street2
        self.rpt_owner_city = rpt_owner_city
        self.rpt_owner_state = rpt_owner_state
        self.rpt_owner_zip_code = rpt_owner_zip_code
        self.rpt_owner_state_description = rpt_owner_state_description

    def __str__(self):
        reporting_owner_address_str = f'rpt_owner_street1: {self.rpt_owner_street1}\n' \
                                      f'rpt_owner_street2: {self.rpt_owner_street2}\n' \
                                      f'rpt_owner_city: {self.rpt_owner_city}\n' \
                                      f'rpt_owner_state: {self.rpt_owner_state}\n' \
                                      f'rpt_owner_zip_code: {self.rpt_owner_zip_code}\n' \
                                      f'rpt_owner_state_description: {self.rpt_owner_state_description}\n'
        return reporting_owner_address_str


class ReportingOwnerRelationship:
    def __init__(self,
                 is_director,
                 is_officer,
                 is_ten_percent_owner,
                 is_other,
                 officer_title,
                 other_text):
        self.is_director = is_director
        self.is_officer = is_officer
        self.is_ten_percent_owner = is_ten_percent_owner
        self.is_other = is_other
        self.officer_title = officer_title
        self.other_text = other_text

    def __str__(self):
        reporting_owner_relationship = f'is_director: {self.is_director}\n' \
                                       f'is_officer: {self.is_officer}\n' \
                                       f'is_ten_percent_owner: {self.is_ten_percent_owner}\n' \
                                       f'is_other: {self.is_other}\n' \
                                       f'officer_title: {self.officer_title}\n' \
                                       f'other_text: {self.other_text}\n'
        return reporting_owner_relationship


class NonDerivativeTransaction:
    def __init__(self,
                 security_title,
                 transaction_date,
                 transaction_form_type,
                 transaction_code,
                 equity_swap_involved,
                 transaction_shares,
                 transaction_price_per_share,
                 transaction_acquire_disposed_code,
                 shares_owner_following_transaction,
                 direct_or_indirect_ownership):
        self.security_title = security_title
        self.transaction_date = transaction_date
        self.transaction_form_type = transaction_form_type
        self.transaction_code = transaction_code
        self.equity_swap_involved = equity_swap_involved
        self.transaction_shares = transaction_shares
        self.transaction_price_per_share = transaction_price_per_share
        self.transaction_acquire_disposed_code = transaction_acquire_disposed_code
        self.shares_owner_following_transaction = shares_owner_following_transaction
        self.direct_or_indirect_ownership = direct_or_indirect_ownership

    def __str__(self):
        non_derivative_transaction_str = f'NonDerivativeTransaction:\n' \
                                         f'security_title: {self.security_title}\n' \
                                         f'transaction_date: {self.transaction_date}\n' \
                                         f'transaction_form_type: {self.transaction_form_type}\n' \
                                         f'transaction_code: {self.transaction_code}\n' \
                                         f'equity_swap_involved: {self.equity_swap_involved}\n' \
                                         f'transaction_shares: {self.transaction_shares}\n' \
                                         f'transaction_price_per_share: {self.transaction_price_per_share}\n' \
                                         f'transaction_acquire_disposed_code: {self.transaction_acquire_disposed_code}\n' \
                                         f'shares_owner_following_transaction: {self.shares_owner_following_transaction}\n' \
                                         f'direct_or_indirect_ownership: {self.direct_or_indirect_ownership}\n'
        return non_derivative_transaction_str


class DerivativeTransaction:
    def __init__(self,
                 security_title,
                 conversion_or_exercise_price,
                 transaction_date,
                 transaction_form_type,
                 transaction_code,
                 equity_swap_involved,
                 transaction_shares,
                 transaction_price_per_share,
                 transaction_acquire_disposed_code,
                 exercise_date,
                 expiration_date,
                 underlying_security_title,
                 underlying_security_shares,
                 shares_owned_following_transaction,
                 direct_or_indirect_ownership):
        self.security_title = security_title
        self.conversion_or_exercise_price = conversion_or_exercise_price
        self.transaction_date = transaction_date
        self.transaction_form_type = transaction_form_type
        self.transaction_code = transaction_code
        self.equity_swap_involved = equity_swap_involved
        self.transaction_shares = transaction_shares
        self.transaction_price_per_share = transaction_price_per_share
        self.transaction_acquire_disposed_code = transaction_acquire_disposed_code
        self.exercise_date = exercise_date
        self.expiration_date = expiration_date
        self.underlying_security_title = underlying_security_title
        self.underlying_security_shares = underlying_security_shares
        self.shares_owned_following_transaction = shares_owned_following_transaction
        self.direct_or_indirect_ownership = direct_or_indirect_ownership

    def __str__(self):
        derivative_transaction_str = f'DerivativeTransaction:\n' \
                                     f'security_title: {self.security_title}\n' \
                                     f'conversion_or_exercise_price: {self.conversion_or_exercise_price}\n' \
                                     f'transaction_date: {self.transaction_date}\n' \
                                     f'transaction_form_type: {self.transaction_form_type}\n' \
                                     f'transaction_code: {self.transaction_code}\n' \
                                     f'equity_swap_involved: {self.equity_swap_involved}\n' \
                                     f'transaction_shares: {self.transaction_shares}\n' \
                                     f'transaction_price_per_share: {self.transaction_price_per_share}\n' \
                                     f'transaction_acquire_disposed_code: {self.transaction_acquire_disposed_code}\n' \
                                     f'exercise_date: {self.exercise_date}\n' \
                                     f'expiration_date: {self.expiration_date}\n' \
                                     f'underlying_security_title: {self.underlying_security_title}\n' \
                                     f'underlying_security_shares: {self.underlying_security_shares}\n' \
                                     f'shares_owned_following_transaction: {self.shares_owned_following_transaction}\n' \
                                     f'direct_or_indirect_ownership: {self.direct_or_indirect_ownership}\n'
        return derivative_transaction_str


class OwnerSignature:
    def __init__(self,
                 signature_name,
                 signature_date):
        self.signature_name = signature_name
        self.signature_date = signature_date

    def __str__(self):
        owner_signature_str = f'signature_name: {self.signature_name}\n' \
                              f'signature_date: {self.signature_date}\n'
        return owner_signature_str


class ReportingOwner:
    def __init__(self,
                 reporting_owner_id,
                 reporting_owner_address,
                 reporting_owner_relationship):
        self.reporting_owner_id = reporting_owner_id
        self.reporting_owner_address = reporting_owner_address
        self.reporting_owner_relationship = reporting_owner_relationship

    def __str__(self):
        reporting_owner_str = f'reporting_owner_id:\n' \
                              f'{self.reporting_owner_id}\n' \
                              f'reporting_owner_address:\n' \
                              f'{self.reporting_owner_address}\n' \
                              f'reporting_owner_relationship:\n' \
                              f'{self.reporting_owner_relationship}\n'
        return reporting_owner_str


class Form4Parser:

    def __init__(self):
        self.schema_version = ''
        self.document_type = ''
        self.period_of_report = ''
        self.issuer = None
        self.reporting_owner = None
        self.non_derivative_table = []
        self.derivative_table = []
        self.owner_signature = None

    def parse(self, str_content):
        print('Start parse!')
        pos1 = str_content.find(b'<XML>')
        pos2 = str_content.find(b'</XML>')
        str_content = str_content[pos1 + 5: pos2].strip(b'\n')
        ownership_document = etree.fromstring(str_content)

        schema_version_node = ownership_document.xpath('//schemaVersion/text()')
        if schema_version_node:
            self.schema_version = schema_version_node[0]

        document_type_node = ownership_document.xpath('//documentType/text()')
        if document_type_node:
            self.document_type = document_type_node[0]

        period_of_report_node = ownership_document.xpath('//periodOfReport/text()')
        if period_of_report_node:
            self.period_of_report = period_of_report_node[0]

        issuer_cik_node = ownership_document.xpath('//issuerCik/text()')
        issuer_cik = ''
        if issuer_cik_node:
            issuer_cik = issuer_cik_node[0]

        issuer_name_node = ownership_document.xpath('//issuerName/text()')
        issuer_name = ''
        if issuer_name_node:
            issuer_name = issuer_name_node[0]

        issuer_trading_symbol_node = ownership_document.xpath('//issuerTradingSymbol/text()')
        issuer_trading_symbol = ''
        if issuer_trading_symbol_node:
            issuer_trading_symbol = issuer_trading_symbol_node[0]

        self.issuer = Issuer(issuer_cik, issuer_name, issuer_trading_symbol)

        rpt_owner_cik_node = ownership_document.xpath('//rptOwnerCik/text()')
        rpt_owner_cik = ''
        if rpt_owner_cik_node:
            rpt_owner_cik = rpt_owner_cik_node[0]

        rpt_owner_name_node = ownership_document.xpath('//rptOwnerName/text()')
        rpt_owner_name = ''
        if rpt_owner_name_node:
            rpt_owner_name = rpt_owner_name_node[0]

        reporting_owner_id = ReportingOwnerId(rpt_owner_cik, rpt_owner_name)

        rpt_owner_street1_node = ownership_document.xpath('//rptOwnerStreet1/text()')
        rpt_owner_street1 = ''
        if rpt_owner_street1_node:
            rpt_owner_street1 = rpt_owner_street1_node[0]

        rpt_owner_street2_node = ownership_document.xpath('//rptOwnerStreet2/text()')
        rpt_owner_street2 = ''
        if rpt_owner_street2_node:
            rpt_owner_street2 = rpt_owner_street2_node[0]

        rpt_owner_city_node = ownership_document.xpath('//rptOwnerCity/text()')
        rpt_owner_city = ''
        if rpt_owner_city_node:
            rpt_owner_city = rpt_owner_city_node[0]

        rpt_owner_state_node = ownership_document.xpath('//rptOwnerState/text()')
        rpt_owner_state = ''
        if rpt_owner_state_node:
            rpt_owner_state = rpt_owner_state_node[0]

        rpt_owner_zip_code_node = ownership_document.xpath('//rptOwnerZipCode/text()')
        rpt_owner_zip_code = ''
        if rpt_owner_zip_code_node:
            rpt_owner_zip_code = rpt_owner_zip_code_node[0]

        rpt_owner_state_description_node = ownership_document.xpath('//rptOwnerStateDescription/text()')
        rpt_owner_state_description = ''
        if rpt_owner_state_description_node:
            rpt_owner_state_description = rpt_owner_state_description_node[0]

        reporting_owner_address = ReportingOwnerAddress(rpt_owner_street1, rpt_owner_street2, rpt_owner_city,
                                                        rpt_owner_state, rpt_owner_zip_code,
                                                        rpt_owner_state_description)

        is_director_node = ownership_document.xpath('//isDirector/text()')
        is_director = ''
        if is_director_node:
            is_director = is_director_node[0]

        is_officer_node = ownership_document.xpath('//isOfficer/text()')
        is_officer = ''
        if is_officer_node:
            is_officer = is_officer_node[0]

        is_ten_percent_owner_node = ownership_document.xpath('//isTenPercentOwner/text()')
        is_ten_percent_owner = ''
        if is_ten_percent_owner_node:
            is_ten_percent_owner = is_ten_percent_owner_node[0]

        is_other_node = ownership_document.xpath('//isOther/text()')
        is_other = ''
        if is_other_node:
            is_other = is_other_node[0]

        officer_title_node = ownership_document.xpath('//officerTitle/text()')
        officer_title = ''
        if officer_title_node:
            officer_title = officer_title_node[0]

        other_text_node = ownership_document.xpath('//otherText/text()')
        other_text = ''
        if other_text_node:
            other_text = other_text_node[0]

        reporting_owner_relationship = ReportingOwnerRelationship(is_director, is_officer, is_ten_percent_owner,
                                                                  is_other, officer_title, other_text)

        self.reporting_owner = ReportingOwner(reporting_owner_id, reporting_owner_address, reporting_owner_relationship)

        non_derivative_transaction_nodes = ownership_document.xpath('//nonDerivativeTable/nonDerivativeTransaction')
        for non_derivative_transaction_node in non_derivative_transaction_nodes:
            security_title_node = non_derivative_transaction_node.xpath('//securityTitle/value/text()')
            security_title = ''
            if security_title_node:
                security_title = security_title_node[0]

            transaction_date_node = non_derivative_transaction_node.xpath('//transactionDate/value/text()')
            transaction_date = ''
            if transaction_date_node:
                transaction_date = transaction_date_node[0]

            transaction_form_type_node = non_derivative_transaction_node.xpath(
                '//transactionCoding/transactionFormType/text()')
            transaction_form_type = ''
            if transaction_form_type_node:
                transaction_form_type = transaction_form_type_node[0]

            transaction_code_node = non_derivative_transaction_node.xpath('//transactionCoding/transactionCode/text()')
            transaction_code = ''
            if transaction_code_node:
                transaction_code = transaction_code_node[0]

            equity_swap_involved_node = non_derivative_transaction_node.xpath(
                '//transactionCoding/equitySwapInvolved/text()')
            equity_swap_involved = ''
            if equity_swap_involved_node:
                equity_swap_involved = equity_swap_involved_node[0]

            transaction_shares_node = non_derivative_transaction_node.xpath(
                '//transactionAmounts/transactionShares/value/text()')
            transaction_shares = ''
            if transaction_shares_node:
                transaction_shares = transaction_shares_node[0]

            transaction_price_per_share_node = non_derivative_transaction_node.xpath(
                '//transactionAmounts/transactionPricePerShare/value/text()')
            transaction_price_per_share = ''
            if transaction_price_per_share_node:
                transaction_price_per_share = transaction_price_per_share_node[0]

            transaction_acquire_disposed_code_node = non_derivative_transaction_node.xpath(
                '//transactionAmounts/transactionAcquiredDisposedCode/value/text()')
            transaction_acquire_disposed_code = ''
            if transaction_acquire_disposed_code_node:
                transaction_acquire_disposed_code = transaction_acquire_disposed_code_node[0]

            shares_owner_following_transaction_node = non_derivative_transaction_node.xpath(
                '//postTransactionAmounts/sharesOwnedFollowingTransaction/value/text()')
            shares_owner_following_transaction = ''
            if shares_owner_following_transaction_node:
                shares_owner_following_transaction = shares_owner_following_transaction_node[0]

            direct_or_indirect_ownership_node = non_derivative_transaction_node.xpath(
                '//ownershipNature/directOrIndirectOwnership/value/text()')
            direct_or_indirect_ownership = ''
            if direct_or_indirect_ownership_node:
                direct_or_indirect_ownership = direct_or_indirect_ownership_node[0]

            non_derivative_transaction = NonDerivativeTransaction(security_title, transaction_date,
                                                                  transaction_form_type, transaction_code,
                                                                  equity_swap_involved, transaction_shares,
                                                                  transaction_price_per_share,
                                                                  transaction_acquire_disposed_code,
                                                                  shares_owner_following_transaction,
                                                                  direct_or_indirect_ownership)
            self.non_derivative_table.append(non_derivative_transaction)

        derivative_transaction_nodes = ownership_document.xpath('//derivativeTable/derivativeTransaction')
        for derivative_transaction_node in derivative_transaction_nodes:
            security_title_node = derivative_transaction_node.xpath('//securityTitle/value/text()')
            security_title = ''
            if security_title_node:
                security_title = security_title_node[0]

            conversion_or_exercise_price_node = derivative_transaction_node.xpath(
                '//conversionOrExercisePrice/value/text()')
            conversion_or_exercise_price = ''
            if conversion_or_exercise_price_node:
                conversion_or_exercise_price = conversion_or_exercise_price_node[0]

            transaction_date_node = derivative_transaction_node.xpath('//transactionDate/value/text()')
            transaction_date = ''
            if transaction_date_node:
                transaction_date = transaction_date_node[0]

            transaction_form_type_node = derivative_transaction_node.xpath(
                '//transactionCoding/transactionFormType/text()')
            transaction_form_type = ''
            if transaction_form_type_node:
                transaction_form_type = transaction_form_type_node[0]

            transaction_code_node = derivative_transaction_node.xpath('//transactionCoding/transactionCode/text()')
            transaction_code = ''
            if transaction_code_node:
                transaction_code = transaction_code_node[0]

            equity_swap_involved_node = derivative_transaction_node.xpath(
                '//transactionCoding/equitySwapInvolved/text()')
            equity_swap_involved = ''
            if equity_swap_involved_node:
                equity_swap_involved = equity_swap_involved_node[0]

            transaction_shares_node = derivative_transaction_node.xpath(
                '//transactionAmounts/transactionShares/value/text()')
            transaction_shares = ''
            if transaction_shares_node:
                transaction_shares = transaction_shares_node[0]

            transaction_price_per_share_node = derivative_transaction_node.xpath(
                '//transactionAmounts/transactionPricePerShare/value/text()')
            transaction_price_per_share = ''
            if transaction_price_per_share_node:
                transaction_price_per_share = transaction_price_per_share_node[0]

            transaction_acquire_disposed_code_node = derivative_transaction_node.xpath(
                '//transactionAmounts/transactionAcquiredDisposedCode/value/text()')
            transaction_acquire_disposed_code = ''
            if transaction_acquire_disposed_code_node:
                transaction_acquire_disposed_code = transaction_acquire_disposed_code_node[0]

            exercise_date_node = derivative_transaction_node.xpath('//exerciseDate/value/text()')
            exercise_date = ''
            if exercise_date_node:
                exercise_date = exercise_date_node[0]

            expiration_date_node = derivative_transaction_node.xpath('//expirationDate/value/text()')
            expiration_date = ''
            if expiration_date_node:
                expiration_date = expiration_date_node[0]

            underlying_security_title_node = derivative_transaction_node.xpath(
                '//underlyingSecurity/underlyingSecurityTitle/value/text()')
            underlying_security_title = ''
            if underlying_security_title_node:
                underlying_security_title = underlying_security_title_node[0]

            underlying_security_shares_node = derivative_transaction_node.xpath(
                '//underlyingSecurity/underlyingSecurityShares/value/text()')
            underlying_security_shares = ''
            if underlying_security_shares_node:
                underlying_security_shares = underlying_security_shares_node[0]

            shares_owned_following_transaction_node = derivative_transaction_node.xpath(
                '//postTransactionAmounts/sharesOwnedFollowingTransaction/value/text()')
            shares_owned_following_transaction = ''
            if shares_owned_following_transaction_node:
                shares_owned_following_transaction = shares_owned_following_transaction_node[0]

            direct_or_indirect_ownership_node = derivative_transaction_node.xpath(
                '//ownershipNature/directOrIndirectOwnership/value/text()')
            direct_or_indirect_ownership = ''
            if direct_or_indirect_ownership_node:
                direct_or_indirect_ownership = direct_or_indirect_ownership_node[0]

            derivative_transaction = DerivativeTransaction(security_title, conversion_or_exercise_price,
                                                           transaction_date, transaction_form_type,
                                                           transaction_code, equity_swap_involved, transaction_shares,
                                                           transaction_price_per_share,
                                                           transaction_acquire_disposed_code, exercise_date,
                                                           expiration_date, underlying_security_title,
                                                           underlying_security_shares,
                                                           shares_owned_following_transaction,
                                                           direct_or_indirect_ownership)
            self.derivative_table.append(derivative_transaction)

        signature_name_node = ownership_document.xpath('//ownerSignature/signatureName/text()')
        signature_name = ''
        if signature_name_node:
            signature_name = signature_name_node[0]

        signature_date_node = ownership_document.xpath('//ownerSignature/signatureDate/text()')
        signature_date = ''
        if signature_date_node:
            signature_date = signature_date_node[0]

        self.owner_signature = OwnerSignature(signature_name, signature_date)

    def save_to_file(self, file_path):
        file_name = os.path.join(file_path, self.period_of_report + '.txt')
        f = open(file_name, 'a+')
        f.write('schema_version: ' + self.schema_version + '\n')
        f.write('document_type: ' + self.document_type + '\n')
        f.write('period_of_report: ' + self.period_of_report + '\n')
        f.write(str(self.issuer))
        f.write(str(self.reporting_owner))
        for non_derivative in self.non_derivative_table:
            f.write(str(non_derivative))
            f.write('\n')

        for derivative in self.derivative_table:
            f.write(str(derivative))
            f.write('\n')

        f.write(str(self.owner_signature))
