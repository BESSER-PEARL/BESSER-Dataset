####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
wikidb116_version116_page_restrictions = Class(name="wikidb116::version116::page::restrictions")
wikidb116_version116_templatelinks = Class(name="wikidb116::version116::templatelinks")
wikidb116_version116_hitcounter = Class(name="wikidb116::version116::hitcounter")
wikidb116_version116_trackbacks = Class(name="wikidb116::version116::trackbacks")
wikidb116_version116_querycache_info = Class(name="wikidb116::version116::querycache::info")
wikidb116_version116_protected_titles = Class(name="wikidb116::version116::protected::titles")
wikidb116_version116_watchlist = Class(name="wikidb116::version116::watchlist")
wikidb116_version116_interwiki = Class(name="wikidb116::version116::interwiki")
wikidb116_version116_job = Class(name="wikidb116::version116::job")
wikidb116_version116_filearchive = Class(name="wikidb116::version116::filearchive")
wikidb116_version116_objectcache = Class(name="wikidb116::version116::objectcache")
wikidb116_version116_image = Class(name="wikidb116::version116::image")
wikidb116_version116_category = Class(name="wikidb116::version116::category")
wikidb116_version116_imagelinks = Class(name="wikidb116::version116::imagelinks")
wikidb116_version116_user = Class(name="wikidb116::version116::user")
wikidb116_version116_revision = Class(name="wikidb116::version116::revision")
wikidb116_version116_updatelog = Class(name="wikidb116::version116::updatelog")
wikidb116_version116_user_groups = Class(name="wikidb116::version116::user::groups")
wikidb116_version116_externallinks = Class(name="wikidb116::version116::externallinks")
wikidb116_version116_searchindex = Class(name="wikidb116::version116::searchindex")
wikidb116_version116_archive = Class(name="wikidb116::version116::archive")
wikidb116_version116_langlinks = Class(name="wikidb116::version116::langlinks")
wikidb116_version116_recentchanges = Class(name="wikidb116::version116::recentchanges")
wikidb116_version116_querycachetwo = Class(name="wikidb116::version116::querycachetwo")
wikidb116_version116_ipblocks = Class(name="wikidb116::version116::ipblocks")
wikidb116_version116_categorylinks = Class(name="wikidb116::version116::categorylinks")
wikidb116_version116_site_stats = Class(name="wikidb116::version116::site::stats")
wikidb116_version116_page = Class(name="wikidb116::version116::page")
wikidb116_version116_external_user = Class(name="wikidb116::version116::external::user")
wikidb116_version116_pagelinks = Class(name="wikidb116::version116::pagelinks")
wikidb116_version116_redirect = Class(name="wikidb116::version116::redirect")
wikidb116_version116_tag_summary = Class(name="wikidb116::version116::tag::summary")
wikidb116_version116_logging = Class(name="wikidb116::version116::logging")
wikidb116_version116_valid_tag = Class(name="wikidb116::version116::valid::tag")
wikidb116_version116_page_props = Class(name="wikidb116::version116::page::props")
wikidb116_version116_user_properties = Class(name="wikidb116::version116::user::properties")
wikidb116_version116_user_newtalk = Class(name="wikidb116::version116::user::newtalk")
wikidb116_version116_text = Class(name="wikidb116::version116::text")
wikidb116_version116_transcache = Class(name="wikidb116::version116::transcache")
wikidb116_version116_change_tag = Class(name="wikidb116::version116::change::tag")
wikidb116_version116_oldimage = Class(name="wikidb116::version116::oldimage")
wikidb116_version116_l10n_cache = Class(name="wikidb116::version116::l10n::cache")
wikidb116_version116_querycache = Class(name="wikidb116::version116::querycache")
wikidb116_version116_log_search = Class(name="wikidb116::version116::log::search")
wikidb116_version116_math = Class(name="wikidb116::version116::math")

# wikidb116_version116_page_restrictions class attributes and methods
wikidb116_version116_page_restrictions_pr_user: Property = Property(name="pr_user", type=StringType)
wikidb116_version116_page_restrictions_pr_type: Property = Property(name="pr_type", type=StringType)
wikidb116_version116_page_restrictions_pr_page: Property = Property(name="pr_page", type=StringType)
wikidb116_version116_page_restrictions_pr_expiry: Property = Property(name="pr_expiry", type=StringType)
wikidb116_version116_page_restrictions_pr_cascade: Property = Property(name="pr_cascade", type=IntegerType)
wikidb116_version116_page_restrictions_pr_id: Property = Property(name="pr_id", type=StringType)
wikidb116_version116_page_restrictions_pr_level: Property = Property(name="pr_level", type=StringType)
wikidb116_version116_page_restrictions.attributes={wikidb116_version116_page_restrictions_pr_type, wikidb116_version116_page_restrictions_pr_user, wikidb116_version116_page_restrictions_pr_cascade, wikidb116_version116_page_restrictions_pr_expiry, wikidb116_version116_page_restrictions_pr_id, wikidb116_version116_page_restrictions_pr_level, wikidb116_version116_page_restrictions_pr_page}

# wikidb116_version116_templatelinks class attributes and methods
wikidb116_version116_templatelinks_tl_from: Property = Property(name="tl_from", type=StringType)
wikidb116_version116_templatelinks_tl_title: Property = Property(name="tl_title", type=StringType)
wikidb116_version116_templatelinks_tl_namespace: Property = Property(name="tl_namespace", type=StringType)
wikidb116_version116_templatelinks.attributes={wikidb116_version116_templatelinks_tl_namespace, wikidb116_version116_templatelinks_tl_title, wikidb116_version116_templatelinks_tl_from}

# wikidb116_version116_hitcounter class attributes and methods
wikidb116_version116_hitcounter_hc_id: Property = Property(name="hc_id", type=StringType)
wikidb116_version116_hitcounter.attributes={wikidb116_version116_hitcounter_hc_id}

# wikidb116_version116_trackbacks class attributes and methods
wikidb116_version116_trackbacks_tb_page: Property = Property(name="tb_page", type=StringType)
wikidb116_version116_trackbacks_tb_name: Property = Property(name="tb_name", type=StringType)
wikidb116_version116_trackbacks_tb_title: Property = Property(name="tb_title", type=StringType)
wikidb116_version116_trackbacks_tb_url: Property = Property(name="tb_url", type=StringType)
wikidb116_version116_trackbacks_tb_ex: Property = Property(name="tb_ex", type=StringType)
wikidb116_version116_trackbacks_tb_id: Property = Property(name="tb_id", type=StringType)
wikidb116_version116_trackbacks.attributes={wikidb116_version116_trackbacks_tb_title, wikidb116_version116_trackbacks_tb_url, wikidb116_version116_trackbacks_tb_name, wikidb116_version116_trackbacks_tb_page, wikidb116_version116_trackbacks_tb_ex, wikidb116_version116_trackbacks_tb_id}

# wikidb116_version116_querycache_info class attributes and methods
wikidb116_version116_querycache_info_qci_type: Property = Property(name="qci_type", type=StringType)
wikidb116_version116_querycache_info_qci_timestamp: Property = Property(name="qci_timestamp", type=StringType)
wikidb116_version116_querycache_info.attributes={wikidb116_version116_querycache_info_qci_type, wikidb116_version116_querycache_info_qci_timestamp}

# wikidb116_version116_protected_titles class attributes and methods
wikidb116_version116_protected_titles_pt_user: Property = Property(name="pt_user", type=StringType)
wikidb116_version116_protected_titles_pt_timestamp: Property = Property(name="pt_timestamp", type=StringType)
wikidb116_version116_protected_titles_pt_namespace: Property = Property(name="pt_namespace", type=StringType)
wikidb116_version116_protected_titles_pt_expiry: Property = Property(name="pt_expiry", type=StringType)
wikidb116_version116_protected_titles_pt_title: Property = Property(name="pt_title", type=StringType)
wikidb116_version116_protected_titles_pt_create_perm: Property = Property(name="pt_create_perm", type=StringType)
wikidb116_version116_protected_titles_pt_reason: Property = Property(name="pt_reason", type=StringType)
wikidb116_version116_protected_titles.attributes={wikidb116_version116_protected_titles_pt_user, wikidb116_version116_protected_titles_pt_reason, wikidb116_version116_protected_titles_pt_timestamp, wikidb116_version116_protected_titles_pt_expiry, wikidb116_version116_protected_titles_pt_create_perm, wikidb116_version116_protected_titles_pt_namespace, wikidb116_version116_protected_titles_pt_title}

# wikidb116_version116_watchlist class attributes and methods
wikidb116_version116_watchlist_wl_title: Property = Property(name="wl_title", type=StringType)
wikidb116_version116_watchlist_wl_namespace: Property = Property(name="wl_namespace", type=StringType)
wikidb116_version116_watchlist_wl_notificationtimestamp: Property = Property(name="wl_notificationtimestamp", type=StringType)
wikidb116_version116_watchlist_wl_user: Property = Property(name="wl_user", type=StringType)
wikidb116_version116_watchlist.attributes={wikidb116_version116_watchlist_wl_namespace, wikidb116_version116_watchlist_wl_notificationtimestamp, wikidb116_version116_watchlist_wl_title, wikidb116_version116_watchlist_wl_user}

# wikidb116_version116_interwiki class attributes and methods
wikidb116_version116_interwiki_iw_url: Property = Property(name="iw_url", type=StringType)
wikidb116_version116_interwiki_iw_trans: Property = Property(name="iw_trans", type=IntegerType)
wikidb116_version116_interwiki_iw_prefix: Property = Property(name="iw_prefix", type=StringType)
wikidb116_version116_interwiki_iw_local: Property = Property(name="iw_local", type=IntegerType)
wikidb116_version116_interwiki.attributes={wikidb116_version116_interwiki_iw_trans, wikidb116_version116_interwiki_iw_prefix, wikidb116_version116_interwiki_iw_url, wikidb116_version116_interwiki_iw_local}

# wikidb116_version116_job class attributes and methods
wikidb116_version116_job_job_namespace: Property = Property(name="job_namespace", type=StringType)
wikidb116_version116_job_job_params: Property = Property(name="job_params", type=StringType)
wikidb116_version116_job_job_title: Property = Property(name="job_title", type=StringType)
wikidb116_version116_job_job_cmd: Property = Property(name="job_cmd", type=StringType)
wikidb116_version116_job_job_id: Property = Property(name="job_id", type=StringType)
wikidb116_version116_job.attributes={wikidb116_version116_job_job_title, wikidb116_version116_job_job_id, wikidb116_version116_job_job_cmd, wikidb116_version116_job_job_namespace, wikidb116_version116_job_job_params}

# wikidb116_version116_filearchive class attributes and methods
wikidb116_version116_filearchive_fa_bits: Property = Property(name="fa_bits", type=StringType)
wikidb116_version116_filearchive_fa_id: Property = Property(name="fa_id", type=StringType)
wikidb116_version116_filearchive_fa_size: Property = Property(name="fa_size", type=StringType)
wikidb116_version116_filearchive_fa_user_text: Property = Property(name="fa_user_text", type=StringType)
wikidb116_version116_filearchive_fa_major_mime: Property = Property(name="fa_major_mime", type=StringType)
wikidb116_version116_filearchive_fa_deleted_timestamp: Property = Property(name="fa_deleted_timestamp", type=StringType)
wikidb116_version116_filearchive_fa_media_type: Property = Property(name="fa_media_type", type=StringType)
wikidb116_version116_filearchive_fa_storage_key: Property = Property(name="fa_storage_key", type=StringType)
wikidb116_version116_filearchive_fa_deleted_reason: Property = Property(name="fa_deleted_reason", type=StringType)
wikidb116_version116_filearchive_fa_archive_name: Property = Property(name="fa_archive_name", type=StringType)
wikidb116_version116_filearchive_fa_name: Property = Property(name="fa_name", type=StringType)
wikidb116_version116_filearchive_fa_user: Property = Property(name="fa_user", type=StringType)
wikidb116_version116_filearchive_fa_timestamp: Property = Property(name="fa_timestamp", type=StringType)
wikidb116_version116_filearchive_fa_deleted_user: Property = Property(name="fa_deleted_user", type=StringType)
wikidb116_version116_filearchive_fa_minor_mime: Property = Property(name="fa_minor_mime", type=StringType)
wikidb116_version116_filearchive_fa_storage_group: Property = Property(name="fa_storage_group", type=StringType)
wikidb116_version116_filearchive_fa_width: Property = Property(name="fa_width", type=StringType)
wikidb116_version116_filearchive_fa_height: Property = Property(name="fa_height", type=StringType)
wikidb116_version116_filearchive_fa_deleted: Property = Property(name="fa_deleted", type=IntegerType)
wikidb116_version116_filearchive_fa_metadata: Property = Property(name="fa_metadata", type=StringType)
wikidb116_version116_filearchive_fa_description: Property = Property(name="fa_description", type=StringType)
wikidb116_version116_filearchive.attributes={wikidb116_version116_filearchive_fa_deleted_timestamp, wikidb116_version116_filearchive_fa_deleted, wikidb116_version116_filearchive_fa_storage_key, wikidb116_version116_filearchive_fa_timestamp, wikidb116_version116_filearchive_fa_minor_mime, wikidb116_version116_filearchive_fa_user_text, wikidb116_version116_filearchive_fa_metadata, wikidb116_version116_filearchive_fa_major_mime, wikidb116_version116_filearchive_fa_deleted_user, wikidb116_version116_filearchive_fa_description, wikidb116_version116_filearchive_fa_storage_group, wikidb116_version116_filearchive_fa_archive_name, wikidb116_version116_filearchive_fa_user, wikidb116_version116_filearchive_fa_name, wikidb116_version116_filearchive_fa_deleted_reason, wikidb116_version116_filearchive_fa_bits, wikidb116_version116_filearchive_fa_height, wikidb116_version116_filearchive_fa_width, wikidb116_version116_filearchive_fa_media_type, wikidb116_version116_filearchive_fa_size, wikidb116_version116_filearchive_fa_id}

# wikidb116_version116_objectcache class attributes and methods
wikidb116_version116_objectcache_exptime: Property = Property(name="exptime", type=DateType)
wikidb116_version116_objectcache_value: Property = Property(name="value", type=StringType)
wikidb116_version116_objectcache_keyname: Property = Property(name="keyname", type=StringType)
wikidb116_version116_objectcache.attributes={wikidb116_version116_objectcache_value, wikidb116_version116_objectcache_keyname, wikidb116_version116_objectcache_exptime}

# wikidb116_version116_image class attributes and methods
wikidb116_version116_image_img_description: Property = Property(name="img_description", type=StringType)
wikidb116_version116_image_img_user: Property = Property(name="img_user", type=StringType)
wikidb116_version116_image_img_bits: Property = Property(name="img_bits", type=StringType)
wikidb116_version116_image_img_minor_mime: Property = Property(name="img_minor_mime", type=StringType)
wikidb116_version116_image_img_height: Property = Property(name="img_height", type=StringType)
wikidb116_version116_image_img_major_mime: Property = Property(name="img_major_mime", type=StringType)
wikidb116_version116_image_img_size: Property = Property(name="img_size", type=StringType)
wikidb116_version116_image_img_metadata: Property = Property(name="img_metadata", type=StringType)
wikidb116_version116_image_img_media_type: Property = Property(name="img_media_type", type=StringType)
wikidb116_version116_image_img_timestamp: Property = Property(name="img_timestamp", type=StringType)
wikidb116_version116_image_img_user_text: Property = Property(name="img_user_text", type=StringType)
wikidb116_version116_image_img_width: Property = Property(name="img_width", type=StringType)
wikidb116_version116_image_img_sha1: Property = Property(name="img_sha1", type=StringType)
wikidb116_version116_image_img_name: Property = Property(name="img_name", type=StringType)
wikidb116_version116_image.attributes={wikidb116_version116_image_img_size, wikidb116_version116_image_img_sha1, wikidb116_version116_image_img_height, wikidb116_version116_image_img_name, wikidb116_version116_image_img_user, wikidb116_version116_image_img_minor_mime, wikidb116_version116_image_img_bits, wikidb116_version116_image_img_timestamp, wikidb116_version116_image_img_width, wikidb116_version116_image_img_media_type, wikidb116_version116_image_img_user_text, wikidb116_version116_image_img_major_mime, wikidb116_version116_image_img_description, wikidb116_version116_image_img_metadata}

# wikidb116_version116_category class attributes and methods
wikidb116_version116_category_cat_id: Property = Property(name="cat_id", type=StringType)
wikidb116_version116_category_cat_title: Property = Property(name="cat_title", type=StringType)
wikidb116_version116_category_cat_files: Property = Property(name="cat_files", type=StringType)
wikidb116_version116_category_cat_hidden: Property = Property(name="cat_hidden", type=IntegerType)
wikidb116_version116_category_cat_subcats: Property = Property(name="cat_subcats", type=StringType)
wikidb116_version116_category_cat_pages: Property = Property(name="cat_pages", type=StringType)
wikidb116_version116_category.attributes={wikidb116_version116_category_cat_hidden, wikidb116_version116_category_cat_files, wikidb116_version116_category_cat_pages, wikidb116_version116_category_cat_subcats, wikidb116_version116_category_cat_title, wikidb116_version116_category_cat_id}

# wikidb116_version116_imagelinks class attributes and methods
wikidb116_version116_imagelinks_il_from: Property = Property(name="il_from", type=StringType)
wikidb116_version116_imagelinks_il_to: Property = Property(name="il_to", type=StringType)
wikidb116_version116_imagelinks.attributes={wikidb116_version116_imagelinks_il_to, wikidb116_version116_imagelinks_il_from}

# wikidb116_version116_user class attributes and methods
wikidb116_version116_user_user_touched: Property = Property(name="user_touched", type=StringType)
wikidb116_version116_user_user_editcount: Property = Property(name="user_editcount", type=StringType)
wikidb116_version116_user_user_email: Property = Property(name="user_email", type=StringType)
wikidb116_version116_user_user_newpassword: Property = Property(name="user_newpassword", type=StringType)
wikidb116_version116_user_user_email_token: Property = Property(name="user_email_token", type=StringType)
wikidb116_version116_user_user_email_token_expires: Property = Property(name="user_email_token_expires", type=StringType)
wikidb116_version116_user_user_name: Property = Property(name="user_name", type=StringType)
wikidb116_version116_user_user_token: Property = Property(name="user_token", type=StringType)
wikidb116_version116_user_user_real_name: Property = Property(name="user_real_name", type=StringType)
wikidb116_version116_user_user_email_authenticated: Property = Property(name="user_email_authenticated", type=StringType)
wikidb116_version116_user_user_newpass_time: Property = Property(name="user_newpass_time", type=StringType)
wikidb116_version116_user_user_options: Property = Property(name="user_options", type=StringType)
wikidb116_version116_user_user_password: Property = Property(name="user_password", type=StringType)
wikidb116_version116_user_user_registration: Property = Property(name="user_registration", type=StringType)
wikidb116_version116_user_user_id: Property = Property(name="user_id", type=StringType)
wikidb116_version116_user.attributes={wikidb116_version116_user_user_real_name, wikidb116_version116_user_user_id, wikidb116_version116_user_user_registration, wikidb116_version116_user_user_email_token, wikidb116_version116_user_user_password, wikidb116_version116_user_user_email, wikidb116_version116_user_user_options, wikidb116_version116_user_user_email_token_expires, wikidb116_version116_user_user_token, wikidb116_version116_user_user_newpass_time, wikidb116_version116_user_user_email_authenticated, wikidb116_version116_user_user_name, wikidb116_version116_user_user_newpassword, wikidb116_version116_user_user_touched, wikidb116_version116_user_user_editcount}

# wikidb116_version116_revision class attributes and methods
wikidb116_version116_revision_rev_minor_edit: Property = Property(name="rev_minor_edit", type=IntegerType)
wikidb116_version116_revision_rev_user_text: Property = Property(name="rev_user_text", type=StringType)
wikidb116_version116_revision_rev_page: Property = Property(name="rev_page", type=StringType)
wikidb116_version116_revision_rev_text_id: Property = Property(name="rev_text_id", type=StringType)
wikidb116_version116_revision_rev_parent_id: Property = Property(name="rev_parent_id", type=StringType)
wikidb116_version116_revision_rev_deleted: Property = Property(name="rev_deleted", type=IntegerType)
wikidb116_version116_revision_rev_timestamp: Property = Property(name="rev_timestamp", type=StringType)
wikidb116_version116_revision_rev_len: Property = Property(name="rev_len", type=StringType)
wikidb116_version116_revision_rev_comment: Property = Property(name="rev_comment", type=StringType)
wikidb116_version116_revision_rev_user: Property = Property(name="rev_user", type=StringType)
wikidb116_version116_revision_rev_id: Property = Property(name="rev_id", type=StringType)
wikidb116_version116_revision.attributes={wikidb116_version116_revision_rev_len, wikidb116_version116_revision_rev_id, wikidb116_version116_revision_rev_user, wikidb116_version116_revision_rev_text_id, wikidb116_version116_revision_rev_user_text, wikidb116_version116_revision_rev_deleted, wikidb116_version116_revision_rev_comment, wikidb116_version116_revision_rev_timestamp, wikidb116_version116_revision_rev_parent_id, wikidb116_version116_revision_rev_page, wikidb116_version116_revision_rev_minor_edit}

# wikidb116_version116_updatelog class attributes and methods
wikidb116_version116_updatelog_ul_key: Property = Property(name="ul_key", type=StringType)
wikidb116_version116_updatelog.attributes={wikidb116_version116_updatelog_ul_key}

# wikidb116_version116_user_groups class attributes and methods
wikidb116_version116_user_groups_ug_group: Property = Property(name="ug_group", type=StringType)
wikidb116_version116_user_groups_ug_user: Property = Property(name="ug_user", type=StringType)
wikidb116_version116_user_groups.attributes={wikidb116_version116_user_groups_ug_user, wikidb116_version116_user_groups_ug_group}

# wikidb116_version116_externallinks class attributes and methods
wikidb116_version116_externallinks_el_index: Property = Property(name="el_index", type=StringType)
wikidb116_version116_externallinks_el_from: Property = Property(name="el_from", type=StringType)
wikidb116_version116_externallinks_el_to: Property = Property(name="el_to", type=StringType)
wikidb116_version116_externallinks.attributes={wikidb116_version116_externallinks_el_to, wikidb116_version116_externallinks_el_from, wikidb116_version116_externallinks_el_index}

# wikidb116_version116_searchindex class attributes and methods
wikidb116_version116_searchindex_si_page: Property = Property(name="si_page", type=StringType)
wikidb116_version116_searchindex_si_text: Property = Property(name="si_text", type=StringType)
wikidb116_version116_searchindex_si_title: Property = Property(name="si_title", type=StringType)
wikidb116_version116_searchindex.attributes={wikidb116_version116_searchindex_si_title, wikidb116_version116_searchindex_si_text, wikidb116_version116_searchindex_si_page}

# wikidb116_version116_archive class attributes and methods
wikidb116_version116_archive_ar_comment: Property = Property(name="ar_comment", type=StringType)
wikidb116_version116_archive_ar_minor_edit: Property = Property(name="ar_minor_edit", type=IntegerType)
wikidb116_version116_archive_ar_flags: Property = Property(name="ar_flags", type=StringType)
wikidb116_version116_archive_ar_page_id: Property = Property(name="ar_page_id", type=StringType)
wikidb116_version116_archive_ar_text_id: Property = Property(name="ar_text_id", type=StringType)
wikidb116_version116_archive_ar_timestamp: Property = Property(name="ar_timestamp", type=StringType)
wikidb116_version116_archive_ar_rev_id: Property = Property(name="ar_rev_id", type=StringType)
wikidb116_version116_archive_ar_user: Property = Property(name="ar_user", type=StringType)
wikidb116_version116_archive_ar_deleted: Property = Property(name="ar_deleted", type=IntegerType)
wikidb116_version116_archive_ar_namespace: Property = Property(name="ar_namespace", type=StringType)
wikidb116_version116_archive_ar_title: Property = Property(name="ar_title", type=StringType)
wikidb116_version116_archive_ar_text: Property = Property(name="ar_text", type=StringType)
wikidb116_version116_archive_ar_parent_id: Property = Property(name="ar_parent_id", type=StringType)
wikidb116_version116_archive_ar_user_text: Property = Property(name="ar_user_text", type=StringType)
wikidb116_version116_archive_ar_len: Property = Property(name="ar_len", type=StringType)
wikidb116_version116_archive.attributes={wikidb116_version116_archive_ar_text, wikidb116_version116_archive_ar_minor_edit, wikidb116_version116_archive_ar_page_id, wikidb116_version116_archive_ar_user, wikidb116_version116_archive_ar_deleted, wikidb116_version116_archive_ar_user_text, wikidb116_version116_archive_ar_flags, wikidb116_version116_archive_ar_comment, wikidb116_version116_archive_ar_text_id, wikidb116_version116_archive_ar_parent_id, wikidb116_version116_archive_ar_len, wikidb116_version116_archive_ar_rev_id, wikidb116_version116_archive_ar_timestamp, wikidb116_version116_archive_ar_title, wikidb116_version116_archive_ar_namespace}

# wikidb116_version116_langlinks class attributes and methods
wikidb116_version116_langlinks_ll_from: Property = Property(name="ll_from", type=StringType)
wikidb116_version116_langlinks_ll_title: Property = Property(name="ll_title", type=StringType)
wikidb116_version116_langlinks_ll_lang: Property = Property(name="ll_lang", type=StringType)
wikidb116_version116_langlinks.attributes={wikidb116_version116_langlinks_ll_title, wikidb116_version116_langlinks_ll_lang, wikidb116_version116_langlinks_ll_from}

# wikidb116_version116_recentchanges class attributes and methods
wikidb116_version116_recentchanges_rc_minor: Property = Property(name="rc_minor", type=IntegerType)
wikidb116_version116_recentchanges_rc_log_type: Property = Property(name="rc_log_type", type=StringType)
wikidb116_version116_recentchanges_rc_new: Property = Property(name="rc_new", type=IntegerType)
wikidb116_version116_recentchanges_rc_new_len: Property = Property(name="rc_new_len", type=StringType)
wikidb116_version116_recentchanges_rc_this_oldid: Property = Property(name="rc_this_oldid", type=StringType)
wikidb116_version116_recentchanges_rc_timestamp: Property = Property(name="rc_timestamp", type=StringType)
wikidb116_version116_recentchanges_rc_type: Property = Property(name="rc_type", type=IntegerType)
wikidb116_version116_recentchanges_rc_cur_time: Property = Property(name="rc_cur_time", type=StringType)
wikidb116_version116_recentchanges_rc_bot: Property = Property(name="rc_bot", type=IntegerType)
wikidb116_version116_recentchanges_rc_user_text: Property = Property(name="rc_user_text", type=StringType)
wikidb116_version116_recentchanges_rc_logid: Property = Property(name="rc_logid", type=StringType)
wikidb116_version116_recentchanges_rc_user: Property = Property(name="rc_user", type=StringType)
wikidb116_version116_recentchanges_rc_log_action: Property = Property(name="rc_log_action", type=StringType)
wikidb116_version116_recentchanges_rc_params: Property = Property(name="rc_params", type=StringType)
wikidb116_version116_recentchanges_rc_comment: Property = Property(name="rc_comment", type=StringType)
wikidb116_version116_recentchanges_rc_ip: Property = Property(name="rc_ip", type=StringType)
wikidb116_version116_recentchanges_rc_old_len: Property = Property(name="rc_old_len", type=StringType)
wikidb116_version116_recentchanges_rc_title: Property = Property(name="rc_title", type=StringType)
wikidb116_version116_recentchanges_rc_moved_to_ns: Property = Property(name="rc_moved_to_ns", type=IntegerType)
wikidb116_version116_recentchanges_rc_id: Property = Property(name="rc_id", type=StringType)
wikidb116_version116_recentchanges_rc_last_oldid: Property = Property(name="rc_last_oldid", type=StringType)
wikidb116_version116_recentchanges_rc_cur_id: Property = Property(name="rc_cur_id", type=StringType)
wikidb116_version116_recentchanges_rc_patrolled: Property = Property(name="rc_patrolled", type=IntegerType)
wikidb116_version116_recentchanges_rc_deleted: Property = Property(name="rc_deleted", type=IntegerType)
wikidb116_version116_recentchanges_rc_namespace: Property = Property(name="rc_namespace", type=StringType)
wikidb116_version116_recentchanges_rc_moved_to_title: Property = Property(name="rc_moved_to_title", type=StringType)
wikidb116_version116_recentchanges.attributes={wikidb116_version116_recentchanges_rc_moved_to_title, wikidb116_version116_recentchanges_rc_cur_id, wikidb116_version116_recentchanges_rc_patrolled, wikidb116_version116_recentchanges_rc_last_oldid, wikidb116_version116_recentchanges_rc_cur_time, wikidb116_version116_recentchanges_rc_log_type, wikidb116_version116_recentchanges_rc_this_oldid, wikidb116_version116_recentchanges_rc_moved_to_ns, wikidb116_version116_recentchanges_rc_ip, wikidb116_version116_recentchanges_rc_id, wikidb116_version116_recentchanges_rc_user, wikidb116_version116_recentchanges_rc_new_len, wikidb116_version116_recentchanges_rc_type, wikidb116_version116_recentchanges_rc_namespace, wikidb116_version116_recentchanges_rc_params, wikidb116_version116_recentchanges_rc_old_len, wikidb116_version116_recentchanges_rc_new, wikidb116_version116_recentchanges_rc_timestamp, wikidb116_version116_recentchanges_rc_bot, wikidb116_version116_recentchanges_rc_title, wikidb116_version116_recentchanges_rc_comment, wikidb116_version116_recentchanges_rc_deleted, wikidb116_version116_recentchanges_rc_minor, wikidb116_version116_recentchanges_rc_user_text, wikidb116_version116_recentchanges_rc_logid, wikidb116_version116_recentchanges_rc_log_action}

# wikidb116_version116_querycachetwo class attributes and methods
wikidb116_version116_querycachetwo_qcc_type: Property = Property(name="qcc_type", type=StringType)
wikidb116_version116_querycachetwo_qcc_namespacetwo: Property = Property(name="qcc_namespacetwo", type=StringType)
wikidb116_version116_querycachetwo_qcc_value: Property = Property(name="qcc_value", type=StringType)
wikidb116_version116_querycachetwo_qcc_titletwo: Property = Property(name="qcc_titletwo", type=StringType)
wikidb116_version116_querycachetwo_qcc_namespace: Property = Property(name="qcc_namespace", type=StringType)
wikidb116_version116_querycachetwo_qcc_title: Property = Property(name="qcc_title", type=StringType)
wikidb116_version116_querycachetwo.attributes={wikidb116_version116_querycachetwo_qcc_titletwo, wikidb116_version116_querycachetwo_qcc_type, wikidb116_version116_querycachetwo_qcc_namespacetwo, wikidb116_version116_querycachetwo_qcc_title, wikidb116_version116_querycachetwo_qcc_value, wikidb116_version116_querycachetwo_qcc_namespace}

# wikidb116_version116_ipblocks class attributes and methods
wikidb116_version116_ipblocks_ipb_auto: Property = Property(name="ipb_auto", type=IntegerType)
wikidb116_version116_ipblocks_ipb_create_account: Property = Property(name="ipb_create_account", type=IntegerType)
wikidb116_version116_ipblocks_ipb_anon_only: Property = Property(name="ipb_anon_only", type=IntegerType)
wikidb116_version116_ipblocks_ipb_block_email: Property = Property(name="ipb_block_email", type=IntegerType)
wikidb116_version116_ipblocks_ipb_by_text: Property = Property(name="ipb_by_text", type=StringType)
wikidb116_version116_ipblocks_ipb_enable_autoblock: Property = Property(name="ipb_enable_autoblock", type=IntegerType)
wikidb116_version116_ipblocks_ipb_id: Property = Property(name="ipb_id", type=StringType)
wikidb116_version116_ipblocks_ipb_reason: Property = Property(name="ipb_reason", type=StringType)
wikidb116_version116_ipblocks_ipb_timestamp: Property = Property(name="ipb_timestamp", type=StringType)
wikidb116_version116_ipblocks_ipb_range_end: Property = Property(name="ipb_range_end", type=StringType)
wikidb116_version116_ipblocks_ipb_allow_usertalk: Property = Property(name="ipb_allow_usertalk", type=IntegerType)
wikidb116_version116_ipblocks_ipb_range_start: Property = Property(name="ipb_range_start", type=StringType)
wikidb116_version116_ipblocks_ipb_expiry: Property = Property(name="ipb_expiry", type=StringType)
wikidb116_version116_ipblocks_ipb_deleted: Property = Property(name="ipb_deleted", type=IntegerType)
wikidb116_version116_ipblocks_ipb_user: Property = Property(name="ipb_user", type=StringType)
wikidb116_version116_ipblocks_ipb_by: Property = Property(name="ipb_by", type=StringType)
wikidb116_version116_ipblocks_ipb_address: Property = Property(name="ipb_address", type=StringType)
wikidb116_version116_ipblocks.attributes={wikidb116_version116_ipblocks_ipb_range_end, wikidb116_version116_ipblocks_ipb_id, wikidb116_version116_ipblocks_ipb_anon_only, wikidb116_version116_ipblocks_ipb_deleted, wikidb116_version116_ipblocks_ipb_range_start, wikidb116_version116_ipblocks_ipb_user, wikidb116_version116_ipblocks_ipb_by_text, wikidb116_version116_ipblocks_ipb_by, wikidb116_version116_ipblocks_ipb_enable_autoblock, wikidb116_version116_ipblocks_ipb_address, wikidb116_version116_ipblocks_ipb_expiry, wikidb116_version116_ipblocks_ipb_block_email, wikidb116_version116_ipblocks_ipb_allow_usertalk, wikidb116_version116_ipblocks_ipb_reason, wikidb116_version116_ipblocks_ipb_auto, wikidb116_version116_ipblocks_ipb_create_account, wikidb116_version116_ipblocks_ipb_timestamp}

# wikidb116_version116_categorylinks class attributes and methods
wikidb116_version116_categorylinks_cl_to: Property = Property(name="cl_to", type=StringType)
wikidb116_version116_categorylinks_cl_from: Property = Property(name="cl_from", type=StringType)
wikidb116_version116_categorylinks_cl_sortkey: Property = Property(name="cl_sortkey", type=StringType)
wikidb116_version116_categorylinks_cl_timestamp: Property = Property(name="cl_timestamp", type=DateType)
wikidb116_version116_categorylinks.attributes={wikidb116_version116_categorylinks_cl_to, wikidb116_version116_categorylinks_cl_timestamp, wikidb116_version116_categorylinks_cl_sortkey, wikidb116_version116_categorylinks_cl_from}

# wikidb116_version116_site_stats class attributes and methods
wikidb116_version116_site_stats_ss_active_users: Property = Property(name="ss_active_users", type=StringType)
wikidb116_version116_site_stats_ss_users: Property = Property(name="ss_users", type=StringType)
wikidb116_version116_site_stats_ss_total_views: Property = Property(name="ss_total_views", type=StringType)
wikidb116_version116_site_stats_ss_images: Property = Property(name="ss_images", type=StringType)
wikidb116_version116_site_stats_ss_total_pages: Property = Property(name="ss_total_pages", type=StringType)
wikidb116_version116_site_stats_ss_total_edits: Property = Property(name="ss_total_edits", type=StringType)
wikidb116_version116_site_stats_ss_good_articles: Property = Property(name="ss_good_articles", type=StringType)
wikidb116_version116_site_stats_ss_admins: Property = Property(name="ss_admins", type=StringType)
wikidb116_version116_site_stats_ss_row_id: Property = Property(name="ss_row_id", type=StringType)
wikidb116_version116_site_stats.attributes={wikidb116_version116_site_stats_ss_users, wikidb116_version116_site_stats_ss_row_id, wikidb116_version116_site_stats_ss_good_articles, wikidb116_version116_site_stats_ss_admins, wikidb116_version116_site_stats_ss_images, wikidb116_version116_site_stats_ss_total_edits, wikidb116_version116_site_stats_ss_total_views, wikidb116_version116_site_stats_ss_active_users, wikidb116_version116_site_stats_ss_total_pages}

# wikidb116_version116_page class attributes and methods
wikidb116_version116_page_page_len: Property = Property(name="page_len", type=StringType)
wikidb116_version116_page_page_touched: Property = Property(name="page_touched", type=StringType)
wikidb116_version116_page_page_is_new: Property = Property(name="page_is_new", type=IntegerType)
wikidb116_version116_page_page_random: Property = Property(name="page_random", type=FloatType)
wikidb116_version116_page_page_id: Property = Property(name="page_id", type=StringType)
wikidb116_version116_page_page_counter: Property = Property(name="page_counter", type=StringType)
wikidb116_version116_page_page_namespace: Property = Property(name="page_namespace", type=StringType)
wikidb116_version116_page_page_restrictions: Property = Property(name="page_restrictions", type=StringType)
wikidb116_version116_page_page_latest: Property = Property(name="page_latest", type=StringType)
wikidb116_version116_page_page_is_redirect: Property = Property(name="page_is_redirect", type=IntegerType)
wikidb116_version116_page_page_title: Property = Property(name="page_title", type=StringType)
wikidb116_version116_page.attributes={wikidb116_version116_page_page_len, wikidb116_version116_page_page_is_new, wikidb116_version116_page_page_random, wikidb116_version116_page_page_latest, wikidb116_version116_page_page_id, wikidb116_version116_page_page_namespace, wikidb116_version116_page_page_counter, wikidb116_version116_page_page_title, wikidb116_version116_page_page_is_redirect, wikidb116_version116_page_page_touched, wikidb116_version116_page_page_restrictions}

# wikidb116_version116_external_user class attributes and methods
wikidb116_version116_external_user_eu_external_id: Property = Property(name="eu_external_id", type=StringType)
wikidb116_version116_external_user_eu_local_id: Property = Property(name="eu_local_id", type=StringType)
wikidb116_version116_external_user.attributes={wikidb116_version116_external_user_eu_local_id, wikidb116_version116_external_user_eu_external_id}

# wikidb116_version116_pagelinks class attributes and methods
wikidb116_version116_pagelinks_pl_from: Property = Property(name="pl_from", type=StringType)
wikidb116_version116_pagelinks_pl_namespace: Property = Property(name="pl_namespace", type=StringType)
wikidb116_version116_pagelinks_pl_title: Property = Property(name="pl_title", type=StringType)
wikidb116_version116_pagelinks.attributes={wikidb116_version116_pagelinks_pl_namespace, wikidb116_version116_pagelinks_pl_title, wikidb116_version116_pagelinks_pl_from}

# wikidb116_version116_redirect class attributes and methods
wikidb116_version116_redirect_rd_fragment: Property = Property(name="rd_fragment", type=StringType)
wikidb116_version116_redirect_rd_namespace: Property = Property(name="rd_namespace", type=StringType)
wikidb116_version116_redirect_rd_from: Property = Property(name="rd_from", type=StringType)
wikidb116_version116_redirect_rd_title: Property = Property(name="rd_title", type=StringType)
wikidb116_version116_redirect_rd_interwiki: Property = Property(name="rd_interwiki", type=StringType)
wikidb116_version116_redirect.attributes={wikidb116_version116_redirect_rd_namespace, wikidb116_version116_redirect_rd_interwiki, wikidb116_version116_redirect_rd_title, wikidb116_version116_redirect_rd_fragment, wikidb116_version116_redirect_rd_from}

# wikidb116_version116_tag_summary class attributes and methods
wikidb116_version116_tag_summary_ts_rc_id: Property = Property(name="ts_rc_id", type=StringType)
wikidb116_version116_tag_summary_ts_rev_id: Property = Property(name="ts_rev_id", type=StringType)
wikidb116_version116_tag_summary_ts_log_id: Property = Property(name="ts_log_id", type=StringType)
wikidb116_version116_tag_summary_ts_tags: Property = Property(name="ts_tags", type=StringType)
wikidb116_version116_tag_summary.attributes={wikidb116_version116_tag_summary_ts_rev_id, wikidb116_version116_tag_summary_ts_tags, wikidb116_version116_tag_summary_ts_log_id, wikidb116_version116_tag_summary_ts_rc_id}

# wikidb116_version116_logging class attributes and methods
wikidb116_version116_logging_log_params: Property = Property(name="log_params", type=StringType)
wikidb116_version116_logging_log_namespace: Property = Property(name="log_namespace", type=StringType)
wikidb116_version116_logging_log_action: Property = Property(name="log_action", type=StringType)
wikidb116_version116_logging_log_timestamp: Property = Property(name="log_timestamp", type=StringType)
wikidb116_version116_logging_log_page: Property = Property(name="log_page", type=StringType)
wikidb116_version116_logging_log_title: Property = Property(name="log_title", type=StringType)
wikidb116_version116_logging_log_user: Property = Property(name="log_user", type=StringType)
wikidb116_version116_logging_log_deleted: Property = Property(name="log_deleted", type=IntegerType)
wikidb116_version116_logging_log_user_text: Property = Property(name="log_user_text", type=StringType)
wikidb116_version116_logging_log_type: Property = Property(name="log_type", type=StringType)
wikidb116_version116_logging_log_id: Property = Property(name="log_id", type=StringType)
wikidb116_version116_logging_log_comment: Property = Property(name="log_comment", type=StringType)
wikidb116_version116_logging.attributes={wikidb116_version116_logging_log_timestamp, wikidb116_version116_logging_log_comment, wikidb116_version116_logging_log_type, wikidb116_version116_logging_log_id, wikidb116_version116_logging_log_title, wikidb116_version116_logging_log_namespace, wikidb116_version116_logging_log_params, wikidb116_version116_logging_log_user_text, wikidb116_version116_logging_log_deleted, wikidb116_version116_logging_log_page, wikidb116_version116_logging_log_user, wikidb116_version116_logging_log_action}

# wikidb116_version116_valid_tag class attributes and methods
wikidb116_version116_valid_tag_vt_tag: Property = Property(name="vt_tag", type=StringType)
wikidb116_version116_valid_tag.attributes={wikidb116_version116_valid_tag_vt_tag}

# wikidb116_version116_page_props class attributes and methods
wikidb116_version116_page_props_pp_page: Property = Property(name="pp_page", type=StringType)
wikidb116_version116_page_props_pp_value: Property = Property(name="pp_value", type=StringType)
wikidb116_version116_page_props_pp_propname: Property = Property(name="pp_propname", type=StringType)
wikidb116_version116_page_props.attributes={wikidb116_version116_page_props_pp_page, wikidb116_version116_page_props_pp_value, wikidb116_version116_page_props_pp_propname}

# wikidb116_version116_user_properties class attributes and methods
wikidb116_version116_user_properties_up_property: Property = Property(name="up_property", type=StringType)
wikidb116_version116_user_properties_up_user: Property = Property(name="up_user", type=StringType)
wikidb116_version116_user_properties_up_value: Property = Property(name="up_value", type=StringType)
wikidb116_version116_user_properties.attributes={wikidb116_version116_user_properties_up_value, wikidb116_version116_user_properties_up_property, wikidb116_version116_user_properties_up_user}

# wikidb116_version116_user_newtalk class attributes and methods
wikidb116_version116_user_newtalk_user_last_timestamp: Property = Property(name="user_last_timestamp", type=StringType)
wikidb116_version116_user_newtalk_user_id: Property = Property(name="user_id", type=StringType)
wikidb116_version116_user_newtalk_user_ip: Property = Property(name="user_ip", type=StringType)
wikidb116_version116_user_newtalk.attributes={wikidb116_version116_user_newtalk_user_id, wikidb116_version116_user_newtalk_user_ip, wikidb116_version116_user_newtalk_user_last_timestamp}

# wikidb116_version116_text class attributes and methods
wikidb116_version116_text_old_flags: Property = Property(name="old_flags", type=StringType)
wikidb116_version116_text_old_text: Property = Property(name="old_text", type=StringType)
wikidb116_version116_text_old_id: Property = Property(name="old_id", type=StringType)
wikidb116_version116_text.attributes={wikidb116_version116_text_old_text, wikidb116_version116_text_old_flags, wikidb116_version116_text_old_id}

# wikidb116_version116_transcache class attributes and methods
wikidb116_version116_transcache_tc_time: Property = Property(name="tc_time", type=StringType)
wikidb116_version116_transcache_tc_url: Property = Property(name="tc_url", type=StringType)
wikidb116_version116_transcache_tc_contents: Property = Property(name="tc_contents", type=StringType)
wikidb116_version116_transcache.attributes={wikidb116_version116_transcache_tc_url, wikidb116_version116_transcache_tc_time, wikidb116_version116_transcache_tc_contents}

# wikidb116_version116_change_tag class attributes and methods
wikidb116_version116_change_tag_ct_params: Property = Property(name="ct_params", type=StringType)
wikidb116_version116_change_tag_ct_rc_id: Property = Property(name="ct_rc_id", type=StringType)
wikidb116_version116_change_tag_ct_rev_id: Property = Property(name="ct_rev_id", type=StringType)
wikidb116_version116_change_tag_ct_log_id: Property = Property(name="ct_log_id", type=StringType)
wikidb116_version116_change_tag_ct_tag: Property = Property(name="ct_tag", type=StringType)
wikidb116_version116_change_tag.attributes={wikidb116_version116_change_tag_ct_params, wikidb116_version116_change_tag_ct_tag, wikidb116_version116_change_tag_ct_rev_id, wikidb116_version116_change_tag_ct_rc_id, wikidb116_version116_change_tag_ct_log_id}

# wikidb116_version116_oldimage class attributes and methods
wikidb116_version116_oldimage_oi_major_mime: Property = Property(name="oi_major_mime", type=StringType)
wikidb116_version116_oldimage_oi_width: Property = Property(name="oi_width", type=StringType)
wikidb116_version116_oldimage_oi_sha1: Property = Property(name="oi_sha1", type=StringType)
wikidb116_version116_oldimage_oi_description: Property = Property(name="oi_description", type=StringType)
wikidb116_version116_oldimage_oi_size: Property = Property(name="oi_size", type=StringType)
wikidb116_version116_oldimage_oi_name: Property = Property(name="oi_name", type=StringType)
wikidb116_version116_oldimage_oi_timestamp: Property = Property(name="oi_timestamp", type=StringType)
wikidb116_version116_oldimage_oi_minor_mime: Property = Property(name="oi_minor_mime", type=StringType)
wikidb116_version116_oldimage_oi_user_text: Property = Property(name="oi_user_text", type=StringType)
wikidb116_version116_oldimage_oi_archive_name: Property = Property(name="oi_archive_name", type=StringType)
wikidb116_version116_oldimage_oi_height: Property = Property(name="oi_height", type=StringType)
wikidb116_version116_oldimage_oi_bits: Property = Property(name="oi_bits", type=StringType)
wikidb116_version116_oldimage_oi_metadata: Property = Property(name="oi_metadata", type=StringType)
wikidb116_version116_oldimage_oi_user: Property = Property(name="oi_user", type=StringType)
wikidb116_version116_oldimage_oi_media_type: Property = Property(name="oi_media_type", type=StringType)
wikidb116_version116_oldimage_oi_deleted: Property = Property(name="oi_deleted", type=IntegerType)
wikidb116_version116_oldimage.attributes={wikidb116_version116_oldimage_oi_timestamp, wikidb116_version116_oldimage_oi_size, wikidb116_version116_oldimage_oi_archive_name, wikidb116_version116_oldimage_oi_bits, wikidb116_version116_oldimage_oi_major_mime, wikidb116_version116_oldimage_oi_metadata, wikidb116_version116_oldimage_oi_description, wikidb116_version116_oldimage_oi_minor_mime, wikidb116_version116_oldimage_oi_sha1, wikidb116_version116_oldimage_oi_name, wikidb116_version116_oldimage_oi_height, wikidb116_version116_oldimage_oi_media_type, wikidb116_version116_oldimage_oi_user, wikidb116_version116_oldimage_oi_deleted, wikidb116_version116_oldimage_oi_user_text, wikidb116_version116_oldimage_oi_width}

# wikidb116_version116_l10n_cache class attributes and methods
wikidb116_version116_l10n_cache_lc_lang: Property = Property(name="lc_lang", type=StringType)
wikidb116_version116_l10n_cache_lc_key: Property = Property(name="lc_key", type=StringType)
wikidb116_version116_l10n_cache_lc_value: Property = Property(name="lc_value", type=StringType)
wikidb116_version116_l10n_cache.attributes={wikidb116_version116_l10n_cache_lc_lang, wikidb116_version116_l10n_cache_lc_key, wikidb116_version116_l10n_cache_lc_value}

# wikidb116_version116_querycache class attributes and methods
wikidb116_version116_querycache_qc_value: Property = Property(name="qc_value", type=StringType)
wikidb116_version116_querycache_qc_type: Property = Property(name="qc_type", type=StringType)
wikidb116_version116_querycache_qc_namespace: Property = Property(name="qc_namespace", type=StringType)
wikidb116_version116_querycache_qc_title: Property = Property(name="qc_title", type=StringType)
wikidb116_version116_querycache.attributes={wikidb116_version116_querycache_qc_type, wikidb116_version116_querycache_qc_namespace, wikidb116_version116_querycache_qc_title, wikidb116_version116_querycache_qc_value}

# wikidb116_version116_log_search class attributes and methods
wikidb116_version116_log_search_ls_log_id: Property = Property(name="ls_log_id", type=StringType)
wikidb116_version116_log_search_ls_field: Property = Property(name="ls_field", type=StringType)
wikidb116_version116_log_search_ls_value: Property = Property(name="ls_value", type=StringType)
wikidb116_version116_log_search.attributes={wikidb116_version116_log_search_ls_value, wikidb116_version116_log_search_ls_log_id, wikidb116_version116_log_search_ls_field}

# wikidb116_version116_math class attributes and methods
wikidb116_version116_math_math_outputhash: Property = Property(name="math_outputhash", type=StringType)
wikidb116_version116_math_math_inputhash: Property = Property(name="math_inputhash", type=StringType)
wikidb116_version116_math_math_html: Property = Property(name="math_html", type=StringType)
wikidb116_version116_math_math_mathml: Property = Property(name="math_mathml", type=StringType)
wikidb116_version116_math_math_html_conservativeness: Property = Property(name="math_html_conservativeness", type=IntegerType)
wikidb116_version116_math.attributes={wikidb116_version116_math_math_outputhash, wikidb116_version116_math_math_inputhash, wikidb116_version116_math_math_mathml, wikidb116_version116_math_math_html, wikidb116_version116_math_math_html_conservativeness}

# Domain Model
domain_model = DomainModel(
    name="wikidb116",
    types={wikidb116_version116_page_restrictions, wikidb116_version116_templatelinks, wikidb116_version116_hitcounter, wikidb116_version116_trackbacks, wikidb116_version116_querycache_info, wikidb116_version116_protected_titles, wikidb116_version116_watchlist, wikidb116_version116_interwiki, wikidb116_version116_job, wikidb116_version116_filearchive, wikidb116_version116_objectcache, wikidb116_version116_image, wikidb116_version116_category, wikidb116_version116_imagelinks, wikidb116_version116_user, wikidb116_version116_revision, wikidb116_version116_updatelog, wikidb116_version116_user_groups, wikidb116_version116_externallinks, wikidb116_version116_searchindex, wikidb116_version116_archive, wikidb116_version116_langlinks, wikidb116_version116_recentchanges, wikidb116_version116_querycachetwo, wikidb116_version116_ipblocks, wikidb116_version116_categorylinks, wikidb116_version116_site_stats, wikidb116_version116_page, wikidb116_version116_external_user, wikidb116_version116_pagelinks, wikidb116_version116_redirect, wikidb116_version116_tag_summary, wikidb116_version116_logging, wikidb116_version116_valid_tag, wikidb116_version116_page_props, wikidb116_version116_user_properties, wikidb116_version116_user_newtalk, wikidb116_version116_text, wikidb116_version116_transcache, wikidb116_version116_change_tag, wikidb116_version116_oldimage, wikidb116_version116_l10n_cache, wikidb116_version116_querycache, wikidb116_version116_log_search, wikidb116_version116_math},
    associations={},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)