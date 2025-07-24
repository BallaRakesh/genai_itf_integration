standard_chartered_bank_page0_combined = """
    You are tasked with creating a JSON mapping of specific fields for a Letter of Credit (LC) application based on extracting each field from a list of elements. If a field is not found in the provided data, map it to ["not found"].

    Also Make use this OCR for better Extraction :{ocr_data}
    - Use this data for fields such as account numbers, dates, and names to improve efficiency and ensure extraction matches their appearance in the document.

    Below are the required fields and their associated extraction elements:
    **beneficiary_name:**
    - Company Name & Address
    - beneficiary in favour of beneficiary's name
    - request letter for import side: name and address of the beneficiary
    - beneficiary company name and address
    - lc application 59 – beneficiary
    - 59: name and address
    
    **advise_by:**
    - issuance of letter of credit: advise by

    **beneficiary_address:**
    - Company Name & Address
    - beneficiary in favour of beneficiary's name
    - request letter for import side: name and address of the beneficiary
    - beneficiary company name and address
    - lc application 59 – beneficiary
    - 59: address of the beneficiary

    **applicant_name:**
    - Applicant ( Company Name & Address )
    - applicant for account of applicant's name
    - request letter for import side: name of the applicant
    - applicant company name and address
    - lc application 50 – applicant
    - 50: name and address

    **applicant_telephone_no:**
    - Tel
    - applicant telephone

    **place_of_receipt:**
    - Place of Receipt
    - shipment details: place of receipt
    - place of receipt
    - port of discharge, can not be the 'place_of_receipt'

    **place_of_destination:**
    - Place of Destination
    - shipment details: final place of delivery destination
    - shipment details: place of destination
    - final destination

    **port_of_loading:**
    - Port of Loading
    - shipment details: port of loading
    - lc application 44e – port of loading/airport of departure
    - 44a: shipment from

    **port_of_discharge:**
    - Port of Discharge
    - shipment details: port of discharge
    - lc application 44f – port of discharge/airport
    - 44b: shipment to

    **latest_shipment_date:**
    - Not later than
    - shipment details: latest shipment date
    - shipment details: not later than
    - lc application 44c – latest date of shipment
    - 44c: latest date

    **ccy:**
    - Currency & Amount
    - lc details: currency
    - for back-to-back lc only: currency and amount
    - lc application 32b – currency code, amount
    - 32b: currency and amount

    **amount:**
    - Currency & Amount
    - lc details: amount in figures
    - for back-to-back lc only: currency and amount
    - lc application 32b – currency code, amount
    - 32b: currency and amount

    **tolerance_plus:**
    - Amount Tolerance
    - lc details: positive tolerance
    - positive amount tolerance
    - lc application 39a – percentage credit amount
    - 39a: percentage plus

    **tolerance_minus:**
    - Amount Tolerance
    - lc details: negative tolerance
    - negative amount tolerance
    - lc application 39a – percentage credit amount
    - 39a: percentage minus

    **expiry_date:**
    - Expiry Date (dd/mm/yy)
    - issuance of letter of credit: expiry date (dd/mm/yy)
    - lc application 31d – date and place of expiry
    - 31d: date of expiry

    **partial_shipment:**
    - Partial Shipment
    - issuance of letter of credit: partial shipment
    - lc application 43p – partial shipments
    - 43p: partial shipments

    **transshipment:**
    - Transhipment
    - issuance of letter of credit: transshipment
    - lc application 43t – transshipment
    - 43t: transshipment

    **description_of_goods_service:**
    - Goods & Services
    - issuance of letter of credit: goods and services
    - lc application 45a – description of goods and/or services
    - 45a: quantity and description

    **lc_ref_no:**
    - export (Master)LC ref
    - for back-to-back lc only: export master lc reference
    - back lc only: export master lc reference

    **issuing_bank:**
    - Issuing Bank
    - for back-to-back lc only: issuing bank
    - 42a: issuing bank

    **for_back_to_back_lc_only_currency_and_amount:**
    - Currency & Amount
    - for back-to-back lc only: currency and amount

    **currency_and_amount_figures_and_words:**
    - [ Figures & Words ]
    - currency and amount: figures and words
    - 32b: amount in words

    **available_with:**
    - L/C Available with
    - request letter for import side: credit available with
    - issuance of letter of credit: lc available with
    - lc application 41a – credit available with
    - 41a: credit available
    - Sometimes, this will be the entry code. Based on the check mark, we need to extract its corresponding value.

    **available_by:**
    - L/C Available
    - request letter for import side: credit available by
    - issuance of letter of credit: lc available by
    - lc application 41d – available with ... by ...
    - 41a: with credit

    **issuance_of_letter_of_credit_in_country_of:**
    - In country of
    - issuance of letter of credit: in country of

    **applicant_contact_person:**
    - Contact Person
    - applicant contact person

    **beneficiary_telephone_no:**
    - Tel
    - beneficiary telephone

    **beneficiary_contact_person:**
    - Contact Person
    - beneficiary contact person

    **is_the_beneficiary_a_related_party:**
    - Is the Beneficiary a Related Party
    - beneficiary: is the beneficiary a related party

    **Example Output:**
    ```json
    {{
        "beneficiary_name": ["not found"],
        "advise_by": ["not found"],
        "beneficiary_address": ["not found"],
        "applicant_name": ["not found"],
        "applicant_telephone_no": ["not found"],
        "place_of_receipt": ["not found"],
        "place_of_destination": ["not found"],
        "port_of_loading": ["not found"],
        "port_of_discharge": ["not found"],
        "latest_shipment_date": ["not found"],
        "ccy": ["not found"],
        "amount": ["not found"],
        "tolerance_plus": ["not found"],
        "tolerance_minus": ["not found"],
        "expiry_date": ["not found"],
        "partial_shipment": ["not found"],
        "transshipment": ["not found"],
        "description_of_goods_service": ["not found"],
        "lc_ref_no": ["not found"],
        "issuing_bank": ["not found"],
        "for_back_to_back_lc_only_currency_and_amount": ["not found"],
        "currency_and_amount_figures_and_words": ["not found"],
        "available_with": ["not found"],
        "available_by": ["not found"],
        "issuance_of_letter_of_credit_in_country_of": ["not found"],
        "applicant_contact_person": ["not found"],
        "beneficiary_telephone_no": ["not found"],
        "beneficiary_contact_person": ["not found"],
        "is_the_beneficiary_a_related_party": ["not found"]
    }}
    ```
    ### Checkbox Handling Logic
    To accurately extract the required fields, incorporate the following logic for interpreting checked checkboxes (marked with ✓, ✗, filled, or similar indicators) in the document. Use this logic to guide the identification of relevant sections and context for field extraction, without generating a separate checkbox extraction output:

    1. **Focus on Checked Checkboxes**: Only consider checkboxes that are visibly checked. Ignore unchecked or empty checkboxes completely.
    2. **Contextual Key Derivation**: Derive contextual keys based on the most logical and relevant text near each checked checkbox, prioritizing proximity (e.g., adjacent labels, headings, or nearby text). Use these keys to identify sections like "Beneficiary," "Applicant," "LC Available with," "Tenor," or "Partial shipment."
    3. **Binary vs. Mutually Exclusive Checkboxes**:
    - For binary checkboxes (e.g., a single checkbox for "Partial shipment allowed"), assign the value "true" to the derived key.
    - For mutually exclusive checkboxes (e.g., a group where one option like "90 days after Shipment Date" is checked), use the specific option text as the value.
    4. **Section Identification**: Identify the main category or section (e.g., "LC Available with," "Tenor") under which a checked checkbox falls. Use this section as a parent context to narrow the search for field values in the OCR data.
    5. **Context-Driven Mapping**:
    - For **beneficiary_name** and **beneficiary_address**, if a checkbox indicates a "Beneficiary" context (e.g., "in_country_of: Beneficiary" is checked), search the OCR data for "Name:" and "Address:" within or near the "Beneficiary" section to extract the corresponding values (e.g., "Name: ATMOS INC" and "Address: QUEENS STREET, FALCON BUILDING, CALIFORNIA USA").
    - For **applicant_name**, if a checkbox indicates an "Applicant" context (e.g., inferred from "issue_lc_same_details"), search the OCR data for "Name:" within or near the "Applicant" section to extract the corresponding value (e.g., "Name: 3M COMPANY").
    - For **charge_account** and **margin_account**, use checkbox context (e.g., "Instructions to Issuing Bank" with a checked "debit all charges" or "debit principal drawings") to confirm the relevant section, then extract the account number or value following the specified extraction elements.
    - For **instructions_to_issuing_bank_in_settlement_debit_principal_drawings_from_our_account**, only include instruction labels associated with checked checkboxes in the "Instructions to Issuing Bank" section.
    6. **Cross-Referencing**: Cross-reference checkbox-derived sections (e.g., "lc_available_with: Advising_Bank") with OCR data to confirm relevance, but only use them to narrow the search scope for the required fields, not as direct values unless explicitly matched.
    7. **Default to ["not found"]**: If no checkbox context or OCR data clearly matches a required field, or if the context is ambiguous, assign ["not found"] to that field.
"""

standard_chartered_bank_page1_combined = """
    You are tasked with creating a JSON mapping of specific fields for a Letter of Credit (LC) application based on extracting each field from a list of elements. If a field is not found in the provided data, map it to ["not found"].

    Also Make use this OCR for better Extraction :{ocr_data}
    - Use this data for fields such as account numbers, dates, and names to improve efficiency and ensure extraction matches their appearance in the document.

    Below are the required fields and their associated extraction elements:
    **documents_required:**
    - Documents required
    - all documents: documents required
    - lc application 46a – documents required
    - 46a: documents

    **description_of_goods_service:**
    - Goods & Services
    - issuance of letter of credit: goods and services
    - lc application 45a – description of goods and/or services
    - 45a: quantity and description

    **consignee:**
    - Consignee
    - document info: consignee

    **freight_info:**
    - Freight
    - document info: freight

    **notify_info:**
    - Notify
    - document info: notify

    **insured_percentage:**
    - Insured Percentage
    - insurance certificate/policy: insured percentage

    **policy_covering:**
    - Covering
    - insurance certificate/policy: covering

    **insurance_open_cover_lodged_with_standard_chartered_bank_sultanate_of_oman_details_of_open_cover:**
    - Details of Open Cover
    - insurance open cover lodged with Standard Chartered Bank, Sultanate of Oman: details of open cover

    **transport_document_original_no_of_documents:**
    - No. of Documents
    - transport document: original number of documents

    **transport_document_copies_no_of_documents:**
    - No. of Documents
    - transport document: copies number of documents

    **delivery_order_delivery_note_original_no_of_documents:**
    - No. of Documents
    - delivery order/delivery note: original number of documents

    **delivery_order_delivery_note_copies_no_of_documents:**
    - No. of Documents
    - delivery order/delivery note: copies number of documents

    **insurance_certificate_policy_original_no_of_documents:**
    - No. of Documents
    - insurance certificate/policy: original number of documents

    **insurance_certificate_policy_copies_no_of_documents:**
    - No. of Documents
    - insurance certificate/policy: copies number of documents

    **Example Output:**
    ```json
    {{
        "documents_required": ["not found"],
        "description_of_goods_service": ["not found"],
        "consignee": ["not found"],
        "freight_info": ["not found"],
        "notify_info": ["not found"],
        "insured_percentage": ["not found"],
        "policy_covering": ["not found"],
        "insurance_open_cover_lodged_with_standard_chartered_bank_sultanate_of_oman_details_of_open_cover": ["not found"],
        "transport_document_original_no_of_documents": ["not found"],
        "transport_document_copies_no_of_documents": ["not found"],
        "delivery_order_delivery_note_original_no_of_documents": ["not found"],
        "delivery_order_delivery_note_copies_no_of_documents": ["not found"],
        "insurance_certificate_policy_original_no_of_documents": ["not found"],
        "insurance_certificate_policy_copies_no_of_documents": ["not found"]
    }}
    ```
    ### Checkbox Handling Logic
    To accurately extract the required fields, incorporate the following logic for interpreting checked checkboxes (marked with ✓, ✗, filled, or similar indicators) in the document. Use this logic to guide the identification of relevant sections and context for field extraction, without generating a separate checkbox extraction output:

    1. **Focus on Checked Checkboxes**: Only consider checkboxes that are visibly checked. Ignore unchecked or empty checkboxes completely.
    2. **Contextual Key Derivation**: Derive contextual keys based on the most logical and relevant text near each checked checkbox, prioritizing proximity (e.g., adjacent labels, headings, or nearby text). Use these keys to identify sections like "Beneficiary," "Applicant," "LC Available with," "Tenor," or "Partial shipment."
    3. **Binary vs. Mutually Exclusive Checkboxes**:
    - For binary checkboxes (e.g., a single checkbox for "Partial shipment allowed"), assign the value "true" to the derived key.
    - For mutually exclusive checkboxes (e.g., a group where one option like "90 days after Shipment Date" is checked), use the specific option text as the value.
    4. **Section Identification**: Identify the main category or section (e.g., "LC Available with," "Tenor") under which a checked checkbox falls. Use this section as a parent context to narrow the search for field values in the OCR data.
    5. **Context-Driven Mapping**:
    - For **beneficiary_name** and **beneficiary_address**, if a checkbox indicates a "Beneficiary" context (e.g., "in_country_of: Beneficiary" is checked), search the OCR data for "Name:" and "Address:" within or near the "Beneficiary" section to extract the corresponding values (e.g., "Name: ATMOS INC" and "Address: QUEENS STREET, FALCON BUILDING, CALIFORNIA USA").
    - For **applicant_name**, if a checkbox indicates an "Applicant" context (e.g., inferred from "issue_lc_same_details"), search the OCR data for "Name:" within or near the "Applicant" section to extract the corresponding value (e.g., "Name: 3M COMPANY").
    - For **charge_account** and **margin_account**, use checkbox context (e.g., "Instructions to Issuing Bank" with a checked "debit all charges" or "debit principal drawings") to confirm the relevant section, then extract the account number or value following the specified extraction elements.
    - For **instructions_to_issuing_bank_in_settlement_debit_principal_drawings_from_our_account**, only include instruction labels associated with checked checkboxes in the "Instructions to Issuing Bank" section.
    6. **Cross-Referencing**: Cross-reference checkbox-derived sections (e.g., "lc_available_with: Advising_Bank") with OCR data to confirm relevance, but only use them to narrow the search scope for the required fields, not as direct values unless explicitly matched.
    7. **Default to ["not found"]**: If no checkbox context or OCR data clearly matches a required field, or if the context is ambiguous, assign ["not found"] to that field.

"""

standard_chartered_bank_page2_combined = """
    You are tasked with creating a JSON mapping of specific fields for a Letter of Credit (LC) application based on extracting each field from a list of elements. If a field is not found in the provided data, map it to ["not found"].

    Also Make use this OCR for better Extraction :{ocr_data}
    - Use this data for fields such as account numbers, dates, and names to improve efficiency and ensure extraction matches their appearance in the document.

    Below are the required fields and their associated extraction elements:
    **confirmation_required:**
    - Confirmation
    - issuance of letter of credit: confirmation
    - lc application 49 – confirmation instructions
    - 49: confirmation instructions
    
    **advising_bank:**
    - request letter for import side: preferred advising bank
    - issuance of letter of credit: advising bank additional conditions
    - lc application: receiver
    - advising bank
    - issuing bank can be the advising bank 
    
    **documents_required:**
    - Attach additional sheets
    - all documents: documents required
    - lc application 46a – documents required
    - 46a: documents

    **additional_conditions:**
    - this filed is a discriptive field, where we need to extract all the content mentioned for the Additional Conditions
    - Additional Conditions:
    - issuance of letter of credit: additional conditions
    - lc application 47a – additional conditions
    - 47a: additional conditions

    **place_of_expiry:**
    - Additional Conditions
    - issuance of letter of credit: place of expiry (additional conditions)
    - 31d: place of expiry

    **confirmation_charges_if_any_are_for_account_of:**
    - Confirmation Charges for account of
    - other charges: lc confirmation charges, if any, are for account of

    **signed_invoices_no_of_documents:**
    - No. of Documents
    - signed invoices: number of documents

    **packing_list_no_of_documents:**
    - No. of Documents
    - packing list: number of documents

    **certificate_of_origin_no_of_documents:**
    - No. of Documents
    - certificate of origin: number of documents

    **charges_if_any_are_for_account_of:**
    - Charges
    - 71b: specify if any charges are for account of

    **Country_of_Origin:**
    - Country of Origin
    - certificate of origin
    - country of origin

    **transferable:**
    - Transferable
    - issuance of letter of credit: transferable

    **advise_through_bank:**
    - Advise Through Bank
    - issuance of letter of credit: advise through bank
    - lc application 57a – advise through bank (BIC/IFSC)
    - advise through bank

    **signed_invoices_original_no_of_documents:**
    - No. of Documents
    - signed invoices: original number of documents

    **signed_invoices_copies_no_of_documents:**
    - No. of Documents
    - signed invoices: copies number of documents

    **packing_list_original_no_of_documents:**
    - No. of Documents
    - packing list: original number of documents

    **packing_list_copies_no_of_documents:**
    - No. of Documents
    - packing list: copies number of documents

    **documents_to_be_presented_within:**
    - Present documents within
    - issuance of letter of credit: present documents within
    - lc application 48 – period of presentation
    - 48: period of presentation

    **additional_amount:**
    - issuance of letter of credit: additional amount (additional conditions)
    - 39c: additional amounts

    **Example Output:**
    ```json
    {{
        "confirmation_required": ["not found"],
        "advising_bank":["not found"]
        "documents_required": ["not found"],
        "additional_conditions": ["not found"],
        "place_of_expiry": ["not found"],
        "confirmation_charges_if_any_are_for_account_of": ["not found"],
        "signed_invoices_no_of_documents": ["not found"],
        "packing_list_no_of_documents": ["not found"],
        "certificate_of_origin_no_of_documents": ["not found"],
        "charges_if_any_are_for_account_of": ["not found"],
        "Country_of_Origin": ["not found"],
        "transferable": ["not found"],
        "advise_through_bank": ["not found"],
        "signed_invoices_original_no_of_documents": ["not found"],
        "signed_invoices_copies_no_of_documents": ["not found"],
        "packing_list_original_no_of_documents": ["not found"],
        "packing_list_copies_no_of_documents": ["not found"],
        "documents_to_be_presented_within": ["not found"],
        "additional_amount": ["not found"]
    }}
    ```
    ### Checkbox Handling Logic
    To accurately extract the required fields, incorporate the following logic for interpreting checked checkboxes (marked with ✓, ✗, filled, or similar indicators) in the document. Use this logic to guide the identification of relevant sections and context for field extraction, without generating a separate checkbox extraction output:

    1. **Focus on Checked Checkboxes**: Only consider checkboxes that are visibly checked. Ignore unchecked or empty checkboxes completely.
    2. **Contextual Key Derivation**: Derive contextual keys based on the most logical and relevant text near each checked checkbox, prioritizing proximity (e.g., adjacent labels, headings, or nearby text). Use these keys to identify sections like "Beneficiary," "Applicant," "LC Available with," "Tenor," or "Partial shipment."
    3. **Binary vs. Mutually Exclusive Checkboxes**:
    - For binary checkboxes (e.g., a single checkbox for "Partial shipment allowed"), assign the value "true" to the derived key.
    - For mutually exclusive checkboxes (e.g., a group where one option like "90 days after Shipment Date" is checked), use the specific option text as the value.
    4. **Section Identification**: Identify the main category or section (e.g., "LC Available with," "Tenor") under which a checked checkbox falls. Use this section as a parent context to narrow the search for field values in the OCR data.
    5. **Context-Driven Mapping**:
    - For **beneficiary_name** and **beneficiary_address**, if a checkbox indicates a "Beneficiary" context (e.g., "in_country_of: Beneficiary" is checked), search the OCR data for "Name:" and "Address:" within or near the "Beneficiary" section to extract the corresponding values (e.g., "Name: ATMOS INC" and "Address: QUEENS STREET, FALCON BUILDING, CALIFORNIA USA").
    - For **applicant_name**, if a checkbox indicates an "Applicant" context (e.g., inferred from "issue_lc_same_details"), search the OCR data for "Name:" within or near the "Applicant" section to extract the corresponding value (e.g., "Name: 3M COMPANY").
    - For **charge_account** and **margin_account**, use checkbox context (e.g., "Instructions to Issuing Bank" with a checked "debit all charges" or "debit principal drawings") to confirm the relevant section, then extract the account number or value following the specified extraction elements.
    - For **instructions_to_issuing_bank_in_settlement_debit_principal_drawings_from_our_account**, only include instruction labels associated with checked checkboxes in the "Instructions to Issuing Bank" section.
    6. **Cross-Referencing**: Cross-reference checkbox-derived sections (e.g., "lc_available_with: Advising_Bank") with OCR data to confirm relevance, but only use them to narrow the search scope for the required fields, not as direct values unless explicitly matched.
    7. **Default to ["not found"]**: If no checkbox context or OCR data clearly matches a required field, or if the context is ambiguous, assign ["not found"] to that field.
"""

standard_chartered_bank_page3_combined  = """
    You are tasked with creating a JSON mapping of specific fields for a Letter of Credit (LC) application based on extracting each field from a list of elements. If a field is not found in the provided data, map it to ["not found"].

    Also Make use this OCR for better Extraction :{ocr_data}
    - Use this data for fields such as account numbers, dates, and names to improve efficiency and ensure extraction matches their appearance in the document.

    Below are the required fields and their associated extraction elements:
    **charge_account:**
    - Debit all charges to our account no
    - authority to debit bank account: commission and charges
    - instructions to issuing bank: debit all charges to our account no
    - Check for the information 'Debit all charges to our account no.:' and assign the corresponding value.

    **margin_account:**
    - authority to debit bank account: cash margin
    - instructions to issuing bank in settlement: debit principal drawings from our account
    - in settlement: debit principal drawings from our account
    - Check for the information 'In settlement, debit principal drawings from our account:' and assign the corresponding value.

    **instructions_to_issuing_bank_in_settlement_debit_principal_drawings_from_our_account:**
    - In settlement, debit principal drawings from our account
    - instructions to issuing bank in settlement: debit principal drawings from our account
    - 78: instructions to the issuing bank
    - Extract only the instruction labels/keys (not the values) that have a check mark (☑ or ✓) from the "Instructions to Issuing Bank" section of the document.
        - Ignore unchecked options.
        - Do not extract the associated values or account numbers.

    **Example Output:**
    ```json
    {{
        "charge_account": ["not found"],
        "margin_account": ["not found"],
        "instructions_to_issuing_bank_in_settlement_debit_principal_drawings_from_our_account": ["not found"]
    }}
    ```
    ### Checkbox Handling Logic
    To accurately extract the required fields, incorporate the following logic for interpreting checked checkboxes (marked with ✓, ✗, filled, or similar indicators) in the document. Use this logic to guide the identification of relevant sections and context for field extraction, without generating a separate checkbox extraction output:

    1. **Focus on Checked Checkboxes**: Only consider checkboxes that are visibly checked. Ignore unchecked or empty checkboxes completely.
    2. **Contextual Key Derivation**: Derive contextual keys based on the most logical and relevant text near each checked checkbox, prioritizing proximity (e.g., adjacent labels, headings, or nearby text). Use these keys to identify sections like "Beneficiary," "Applicant," "LC Available with," "Tenor," or "Partial shipment."
    3. **Binary vs. Mutually Exclusive Checkboxes**:
    - For binary checkboxes (e.g., a single checkbox for "Partial shipment allowed"), assign the value "true" to the derived key.
    - For mutually exclusive checkboxes (e.g., a group where one option like "90 days after Shipment Date" is checked), use the specific option text as the value.
    4. **Section Identification**: Identify the main category or section (e.g., "LC Available with," "Tenor") under which a checked checkbox falls. Use this section as a parent context to narrow the search for field values in the OCR data.
    5. **Context-Driven Mapping**:
    - For **beneficiary_name** and **beneficiary_address**, if a checkbox indicates a "Beneficiary" context (e.g., "in_country_of: Beneficiary" is checked), search the OCR data for "Name:" and "Address:" within or near the "Beneficiary" section to extract the corresponding values (e.g., "Name: ATMOS INC" and "Address: QUEENS STREET, FALCON BUILDING, CALIFORNIA USA").
    - For **applicant_name**, if a checkbox indicates an "Applicant" context (e.g., inferred from "issue_lc_same_details"), search the OCR data for "Name:" within or near the "Applicant" section to extract the corresponding value (e.g., "Name: 3M COMPANY").
    - For **charge_account** and **margin_account**, use checkbox context (e.g., "Instructions to Issuing Bank" with a checked "debit all charges" or "debit principal drawings") to confirm the relevant section, then extract the account number or value following the specified extraction elements.
    - For **instructions_to_issuing_bank_in_settlement_debit_principal_drawings_from_our_account**, only include instruction labels associated with checked checkboxes in the "Instructions to Issuing Bank" section.
    6. **Cross-Referencing**: Cross-reference checkbox-derived sections (e.g., "lc_available_with: Advising_Bank") with OCR data to confirm relevance, but only use them to narrow the search scope for the required fields, not as direct values unless explicitly matched.
    7. **Default to ["not found"]**: If no checkbox context or OCR data clearly matches a required field, or if the context is ambiguous, assign ["not found"] to that field.

"""

