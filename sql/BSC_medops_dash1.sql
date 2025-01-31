SELECT DISTINCT
    date_trunc('month',transaction_date)::date                      as date_month
    ,cast(Extract(year from transaction_date) as int4)            as date_year
    ,product
    ,count(distinct transaction_id)                                                                         as all_transaction_count
    ,count(distinct case when valid_request =   true then transaction_id end)                               as valid_transactions
    ,count(distinct case when valid_request =   true and duplicate  =   false then transaction_id end)      as valid_dedup_transactions
    ,count(distinct safe.id)                                                                                as distinct_members
FROM reporting.fct_ddp as fd
    left join reporting.rpt_safe_unique_patient_ids as safe
        on fd.patient_id    =   safe.id
where payer  =   'BSC'
group by 1,2,3