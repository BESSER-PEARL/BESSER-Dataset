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
wikidb119_site_stats = Class(name="wikidb119::site::stats")
wikidb119_searchindex = Class(name="wikidb119::searchindex")
wikidb119_pagelinks = Class(name="wikidb119::pagelinks")
wikidb119_user_properties = Class(name="wikidb119::user::properties")
wikidb119_revision = Class(name="wikidb119::revision")
wikidb119_user_former_groups = Class(name="wikidb119::user::former::groups")
wikidb119_imagelinks = Class(name="wikidb119::imagelinks")
wikidb119_text = Class(name="wikidb119::text")
wikidb119_watchlist = Class(name="wikidb119::watchlist")
wikidb119_categorylinks = Class(name="wikidb119::categorylinks")
wikidb119_langlinks = Class(name="wikidb119::langlinks")
wikidb119_transcache = Class(name="wikidb119::transcache")
wikidb119_category = Class(name="wikidb119::category")
wikidb119_msg_resource = Class(name="wikidb119::msg::resource")
wikidb119_job = Class(name="wikidb119::job")
wikidb119_querycachetwo = Class(name="wikidb119::querycachetwo")
wikidb119_redirect = Class(name="wikidb119::redirect")
wikidb119_msg_resource_links = Class(name="wikidb119::msg::resource::links")
wikidb119_externallinks = Class(name="wikidb119::externallinks")
wikidb119_page_props = Class(name="wikidb119::page::props")
wikidb119_templatelinks = Class(name="wikidb119::templatelinks")
wikidb119_uploadstash = Class(name="wikidb119::uploadstash")
wikidb119_image = Class(name="wikidb119::image")
wikidb119_iwlinks = Class(name="wikidb119::iwlinks")
wikidb119_change_tag = Class(name="wikidb119::change::tag")
wikidb119_valid_tag = Class(name="wikidb119::valid::tag")
wikidb119_interwiki = Class(name="wikidb119::interwiki")
wikidb119_external_user = Class(name="wikidb119::external::user")
wikidb119_module_deps = Class(name="wikidb119::module::deps")
wikidb119_querycache = Class(name="wikidb119::querycache")
wikidb119_logging = Class(name="wikidb119::logging")
wikidb119_tag_summary = Class(name="wikidb119::tag::summary")
wikidb119_objectcache = Class(name="wikidb119::objectcache")
wikidb119_protected_titles = Class(name="wikidb119::protected::titles")
wikidb119_recentchanges = Class(name="wikidb119::recentchanges")
wikidb119_page_restrictions = Class(name="wikidb119::page::restrictions")
wikidb119_log_search = Class(name="wikidb119::log::search")
wikidb119_user_groups = Class(name="wikidb119::user::groups")
wikidb119_user_newtalk = Class(name="wikidb119::user::newtalk")
wikidb119_filearchive = Class(name="wikidb119::filearchive")
wikidb119_ipblocks = Class(name="wikidb119::ipblocks")
wikidb119_hitcounter = Class(name="wikidb119::hitcounter")
wikidb119_l10n_cache = Class(name="wikidb119::l10n::cache")
wikidb119_page = Class(name="wikidb119::page")
wikidb119_archive = Class(name="wikidb119::archive")
wikidb119_oldimage = Class(name="wikidb119::oldimage")
wikidb119_updatelog = Class(name="wikidb119::updatelog")
wikidb119_user = Class(name="wikidb119::user")
wikidb119_querycache_info = Class(name="wikidb119::querycache::info")

# wikidb119_site_stats class attributes and methods
wikidb119_site_stats_ss_active_users: Property = Property(name="ss_active_users", type=StringType)
wikidb119_site_stats_ss_users: Property = Property(name="ss_users", type=StringType)
wikidb119_site_stats_ss_total_views: Property = Property(name="ss_total_views", type=StringType)
wikidb119_site_stats_ss_images: Property = Property(name="ss_images", type=StringType)
wikidb119_site_stats_ss_total_pages: Property = Property(name="ss_total_pages", type=StringType)
wikidb119_site_stats_ss_total_edits: Property = Property(name="ss_total_edits", type=StringType)
wikidb119_site_stats_ss_good_articles: Property = Property(name="ss_good_articles", type=StringType)
wikidb119_site_stats_ss_admins: Property = Property(name="ss_admins", type=StringType)
wikidb119_site_stats_ss_row_id: Property = Property(name="ss_row_id", type=StringType)
wikidb119_site_stats.attributes={wikidb119_site_stats_ss_good_articles, wikidb119_site_stats_ss_total_pages, wikidb119_site_stats_ss_images, wikidb119_site_stats_ss_active_users, wikidb119_site_stats_ss_admins, wikidb119_site_stats_ss_users, wikidb119_site_stats_ss_total_edits, wikidb119_site_stats_ss_row_id, wikidb119_site_stats_ss_total_views}

# wikidb119_searchindex class attributes and methods
wikidb119_searchindex_si_page: Property = Property(name="si_page", type=StringType)
wikidb119_searchindex_si_text: Property = Property(name="si_text", type=StringType)
wikidb119_searchindex_si_title: Property = Property(name="si_title", type=StringType)
wikidb119_searchindex.attributes={wikidb119_searchindex_si_text, wikidb119_searchindex_si_page, wikidb119_searchindex_si_title}

# wikidb119_pagelinks class attributes and methods
wikidb119_pagelinks_pl_title: Property = Property(name="pl_title", type=StringType)
wikidb119_pagelinks_pl_from: Property = Property(name="pl_from", type=StringType)
wikidb119_pagelinks_pl_namespace: Property = Property(name="pl_namespace", type=StringType)
wikidb119_pagelinks.attributes={wikidb119_pagelinks_pl_from, wikidb119_pagelinks_pl_namespace, wikidb119_pagelinks_pl_title}

# wikidb119_user_properties class attributes and methods
wikidb119_user_properties_up_property: Property = Property(name="up_property", type=StringType)
wikidb119_user_properties_up_user: Property = Property(name="up_user", type=StringType)
wikidb119_user_properties_up_value: Property = Property(name="up_value", type=StringType)
wikidb119_user_properties.attributes={wikidb119_user_properties_up_property, wikidb119_user_properties_up_value, wikidb119_user_properties_up_user}

# wikidb119_revision class attributes and methods
wikidb119_revision_rev_comment: Property = Property(name="rev_comment", type=StringType)
wikidb119_revision_rev_user: Property = Property(name="rev_user", type=StringType)
wikidb119_revision_rev_id: Property = Property(name="rev_id", type=StringType)
wikidb119_revision_rev_user_text: Property = Property(name="rev_user_text", type=StringType)
wikidb119_revision_rev_page: Property = Property(name="rev_page", type=StringType)
wikidb119_revision_rev_text_id: Property = Property(name="rev_text_id", type=StringType)
wikidb119_revision_rev_sha1: Property = Property(name="rev_sha1", type=StringType)
wikidb119_revision_rev_parent_id: Property = Property(name="rev_parent_id", type=StringType)
wikidb119_revision_rev_deleted: Property = Property(name="rev_deleted", type=IntegerType)
wikidb119_revision_rev_timestamp: Property = Property(name="rev_timestamp", type=StringType)
wikidb119_revision_rev_len: Property = Property(name="rev_len", type=StringType)
wikidb119_revision_rev_minor_edit: Property = Property(name="rev_minor_edit", type=IntegerType)
wikidb119_revision.attributes={wikidb119_revision_rev_user, wikidb119_revision_rev_minor_edit, wikidb119_revision_rev_comment, wikidb119_revision_rev_sha1, wikidb119_revision_rev_timestamp, wikidb119_revision_rev_len, wikidb119_revision_rev_deleted, wikidb119_revision_rev_parent_id, wikidb119_revision_rev_text_id, wikidb119_revision_rev_user_text, wikidb119_revision_rev_id, wikidb119_revision_rev_page}

# wikidb119_user_former_groups class attributes and methods
wikidb119_user_former_groups_ufg_user: Property = Property(name="ufg_user", type=StringType)
wikidb119_user_former_groups_ufg_group: Property = Property(name="ufg_group", type=StringType)
wikidb119_user_former_groups.attributes={wikidb119_user_former_groups_ufg_group, wikidb119_user_former_groups_ufg_user}

# wikidb119_imagelinks class attributes and methods
wikidb119_imagelinks_il_from: Property = Property(name="il_from", type=StringType)
wikidb119_imagelinks_il_to: Property = Property(name="il_to", type=StringType)
wikidb119_imagelinks.attributes={wikidb119_imagelinks_il_from, wikidb119_imagelinks_il_to}

# wikidb119_text class attributes and methods
wikidb119_text_old_flags: Property = Property(name="old_flags", type=StringType)
wikidb119_text_old_text: Property = Property(name="old_text", type=StringType)
wikidb119_text_old_id: Property = Property(name="old_id", type=StringType)
wikidb119_text.attributes={wikidb119_text_old_id, wikidb119_text_old_text, wikidb119_text_old_flags}

# wikidb119_watchlist class attributes and methods
wikidb119_watchlist_wl_title: Property = Property(name="wl_title", type=StringType)
wikidb119_watchlist_wl_namespace: Property = Property(name="wl_namespace", type=StringType)
wikidb119_watchlist_wl_notificationtimestamp: Property = Property(name="wl_notificationtimestamp", type=StringType)
wikidb119_watchlist_wl_user: Property = Property(name="wl_user", type=StringType)
wikidb119_watchlist.attributes={wikidb119_watchlist_wl_user, wikidb119_watchlist_wl_title, wikidb119_watchlist_wl_namespace, wikidb119_watchlist_wl_notificationtimestamp}

# wikidb119_categorylinks class attributes and methods
wikidb119_categorylinks_cl_to: Property = Property(name="cl_to", type=StringType)
wikidb119_categorylinks_cl_from: Property = Property(name="cl_from", type=StringType)
wikidb119_categorylinks_cl_type: Property = Property(name="cl_type", type=StringType)
wikidb119_categorylinks_cl_sortkey_prefix: Property = Property(name="cl_sortkey_prefix", type=StringType)
wikidb119_categorylinks_cl_sortkey: Property = Property(name="cl_sortkey", type=StringType)
wikidb119_categorylinks_cl_timestamp: Property = Property(name="cl_timestamp", type=DateType)
wikidb119_categorylinks_cl_collation: Property = Property(name="cl_collation", type=StringType)
wikidb119_categorylinks.attributes={wikidb119_categorylinks_cl_sortkey_prefix, wikidb119_categorylinks_cl_from, wikidb119_categorylinks_cl_type, wikidb119_categorylinks_cl_timestamp, wikidb119_categorylinks_cl_collation, wikidb119_categorylinks_cl_to, wikidb119_categorylinks_cl_sortkey}

# wikidb119_langlinks class attributes and methods
wikidb119_langlinks_ll_lang: Property = Property(name="ll_lang", type=StringType)
wikidb119_langlinks_ll_from: Property = Property(name="ll_from", type=StringType)
wikidb119_langlinks_ll_title: Property = Property(name="ll_title", type=StringType)
wikidb119_langlinks.attributes={wikidb119_langlinks_ll_title, wikidb119_langlinks_ll_from, wikidb119_langlinks_ll_lang}

# wikidb119_transcache class attributes and methods
wikidb119_transcache_tc_time: Property = Property(name="tc_time", type=StringType)
wikidb119_transcache_tc_url: Property = Property(name="tc_url", type=StringType)
wikidb119_transcache_tc_contents: Property = Property(name="tc_contents", type=StringType)
wikidb119_transcache.attributes={wikidb119_transcache_tc_contents, wikidb119_transcache_tc_time, wikidb119_transcache_tc_url}

# wikidb119_category class attributes and methods
wikidb119_category_cat_id: Property = Property(name="cat_id", type=StringType)
wikidb119_category_cat_title: Property = Property(name="cat_title", type=StringType)
wikidb119_category_cat_files: Property = Property(name="cat_files", type=StringType)
wikidb119_category_cat_hidden: Property = Property(name="cat_hidden", type=IntegerType)
wikidb119_category_cat_subcats: Property = Property(name="cat_subcats", type=StringType)
wikidb119_category_cat_pages: Property = Property(name="cat_pages", type=StringType)
wikidb119_category.attributes={wikidb119_category_cat_subcats, wikidb119_category_cat_files, wikidb119_category_cat_id, wikidb119_category_cat_title, wikidb119_category_cat_pages, wikidb119_category_cat_hidden}

# wikidb119_msg_resource class attributes and methods
wikidb119_msg_resource_mr_timestamp: Property = Property(name="mr_timestamp", type=StringType)
wikidb119_msg_resource_mr_lang: Property = Property(name="mr_lang", type=StringType)
wikidb119_msg_resource_mr_resource: Property = Property(name="mr_resource", type=StringType)
wikidb119_msg_resource_mr_blob: Property = Property(name="mr_blob", type=StringType)
wikidb119_msg_resource.attributes={wikidb119_msg_resource_mr_blob, wikidb119_msg_resource_mr_resource, wikidb119_msg_resource_mr_lang, wikidb119_msg_resource_mr_timestamp}

# wikidb119_job class attributes and methods
wikidb119_job_job_namespace: Property = Property(name="job_namespace", type=StringType)
wikidb119_job_job_params: Property = Property(name="job_params", type=StringType)
wikidb119_job_job_title: Property = Property(name="job_title", type=StringType)
wikidb119_job_job_cmd: Property = Property(name="job_cmd", type=StringType)
wikidb119_job_job_timestamp: Property = Property(name="job_timestamp", type=StringType)
wikidb119_job_job_id: Property = Property(name="job_id", type=StringType)
wikidb119_job.attributes={wikidb119_job_job_namespace, wikidb119_job_job_id, wikidb119_job_job_cmd, wikidb119_job_job_params, wikidb119_job_job_timestamp, wikidb119_job_job_title}

# wikidb119_querycachetwo class attributes and methods
wikidb119_querycachetwo_qcc_namespace: Property = Property(name="qcc_namespace", type=StringType)
wikidb119_querycachetwo_qcc_title: Property = Property(name="qcc_title", type=StringType)
wikidb119_querycachetwo_qcc_type: Property = Property(name="qcc_type", type=StringType)
wikidb119_querycachetwo_qcc_namespacetwo: Property = Property(name="qcc_namespacetwo", type=StringType)
wikidb119_querycachetwo_qcc_value: Property = Property(name="qcc_value", type=StringType)
wikidb119_querycachetwo_qcc_titletwo: Property = Property(name="qcc_titletwo", type=StringType)
wikidb119_querycachetwo.attributes={wikidb119_querycachetwo_qcc_title, wikidb119_querycachetwo_qcc_namespace, wikidb119_querycachetwo_qcc_titletwo, wikidb119_querycachetwo_qcc_type, wikidb119_querycachetwo_qcc_value, wikidb119_querycachetwo_qcc_namespacetwo}

# wikidb119_redirect class attributes and methods
wikidb119_redirect_rd_fragment: Property = Property(name="rd_fragment", type=StringType)
wikidb119_redirect_rd_namespace: Property = Property(name="rd_namespace", type=StringType)
wikidb119_redirect_rd_from: Property = Property(name="rd_from", type=StringType)
wikidb119_redirect_rd_title: Property = Property(name="rd_title", type=StringType)
wikidb119_redirect_rd_interwiki: Property = Property(name="rd_interwiki", type=StringType)
wikidb119_redirect.attributes={wikidb119_redirect_rd_from, wikidb119_redirect_rd_title, wikidb119_redirect_rd_interwiki, wikidb119_redirect_rd_namespace, wikidb119_redirect_rd_fragment}

# wikidb119_msg_resource_links class attributes and methods
wikidb119_msg_resource_links_mrl_resource: Property = Property(name="mrl_resource", type=StringType)
wikidb119_msg_resource_links_mrl_message: Property = Property(name="mrl_message", type=StringType)
wikidb119_msg_resource_links.attributes={wikidb119_msg_resource_links_mrl_resource, wikidb119_msg_resource_links_mrl_message}

# wikidb119_externallinks class attributes and methods
wikidb119_externallinks_el_index: Property = Property(name="el_index", type=StringType)
wikidb119_externallinks_el_from: Property = Property(name="el_from", type=StringType)
wikidb119_externallinks_el_to: Property = Property(name="el_to", type=StringType)
wikidb119_externallinks.attributes={wikidb119_externallinks_el_to, wikidb119_externallinks_el_index, wikidb119_externallinks_el_from}

# wikidb119_page_props class attributes and methods
wikidb119_page_props_pp_page: Property = Property(name="pp_page", type=StringType)
wikidb119_page_props_pp_value: Property = Property(name="pp_value", type=StringType)
wikidb119_page_props_pp_propname: Property = Property(name="pp_propname", type=StringType)
wikidb119_page_props.attributes={wikidb119_page_props_pp_value, wikidb119_page_props_pp_page, wikidb119_page_props_pp_propname}

# wikidb119_templatelinks class attributes and methods
wikidb119_templatelinks_tl_title: Property = Property(name="tl_title", type=StringType)
wikidb119_templatelinks_tl_namespace: Property = Property(name="tl_namespace", type=StringType)
wikidb119_templatelinks_tl_from: Property = Property(name="tl_from", type=StringType)
wikidb119_templatelinks.attributes={wikidb119_templatelinks_tl_namespace, wikidb119_templatelinks_tl_from, wikidb119_templatelinks_tl_title}

# wikidb119_uploadstash class attributes and methods
wikidb119_uploadstash_us_key: Property = Property(name="us_key", type=StringType)
wikidb119_uploadstash_us_media_type: Property = Property(name="us_media_type", type=StringType)
wikidb119_uploadstash_us_user: Property = Property(name="us_user", type=StringType)
wikidb119_uploadstash_us_status: Property = Property(name="us_status", type=StringType)
wikidb119_uploadstash_us_chunk_inx: Property = Property(name="us_chunk_inx", type=StringType)
wikidb119_uploadstash_us_orig_path: Property = Property(name="us_orig_path", type=StringType)
wikidb119_uploadstash_us_id: Property = Property(name="us_id", type=StringType)
wikidb119_uploadstash_us_image_width: Property = Property(name="us_image_width", type=StringType)
wikidb119_uploadstash_us_image_bits: Property = Property(name="us_image_bits", type=IntegerType)
wikidb119_uploadstash_us_image_height: Property = Property(name="us_image_height", type=StringType)
wikidb119_uploadstash_us_path: Property = Property(name="us_path", type=StringType)
wikidb119_uploadstash_us_sha1: Property = Property(name="us_sha1", type=StringType)
wikidb119_uploadstash_us_timestamp: Property = Property(name="us_timestamp", type=StringType)
wikidb119_uploadstash_us_size: Property = Property(name="us_size", type=StringType)
wikidb119_uploadstash_us_source_type: Property = Property(name="us_source_type", type=StringType)
wikidb119_uploadstash_us_mime: Property = Property(name="us_mime", type=StringType)
wikidb119_uploadstash.attributes={wikidb119_uploadstash_us_status, wikidb119_uploadstash_us_source_type, wikidb119_uploadstash_us_image_width, wikidb119_uploadstash_us_mime, wikidb119_uploadstash_us_key, wikidb119_uploadstash_us_chunk_inx, wikidb119_uploadstash_us_path, wikidb119_uploadstash_us_user, wikidb119_uploadstash_us_timestamp, wikidb119_uploadstash_us_size, wikidb119_uploadstash_us_orig_path, wikidb119_uploadstash_us_image_height, wikidb119_uploadstash_us_sha1, wikidb119_uploadstash_us_media_type, wikidb119_uploadstash_us_image_bits, wikidb119_uploadstash_us_id}

# wikidb119_image class attributes and methods
wikidb119_image_img_minor_mime: Property = Property(name="img_minor_mime", type=StringType)
wikidb119_image_img_description: Property = Property(name="img_description", type=StringType)
wikidb119_image_img_height: Property = Property(name="img_height", type=StringType)
wikidb119_image_img_major_mime: Property = Property(name="img_major_mime", type=StringType)
wikidb119_image_img_user: Property = Property(name="img_user", type=StringType)
wikidb119_image_img_bits: Property = Property(name="img_bits", type=StringType)
wikidb119_image_img_size: Property = Property(name="img_size", type=StringType)
wikidb119_image_img_metadata: Property = Property(name="img_metadata", type=StringType)
wikidb119_image_img_media_type: Property = Property(name="img_media_type", type=StringType)
wikidb119_image_img_timestamp: Property = Property(name="img_timestamp", type=StringType)
wikidb119_image_img_user_text: Property = Property(name="img_user_text", type=StringType)
wikidb119_image_img_width: Property = Property(name="img_width", type=StringType)
wikidb119_image_img_sha1: Property = Property(name="img_sha1", type=StringType)
wikidb119_image_img_name: Property = Property(name="img_name", type=StringType)
wikidb119_image.attributes={wikidb119_image_img_size, wikidb119_image_img_bits, wikidb119_image_img_width, wikidb119_image_img_minor_mime, wikidb119_image_img_sha1, wikidb119_image_img_description, wikidb119_image_img_major_mime, wikidb119_image_img_user_text, wikidb119_image_img_name, wikidb119_image_img_media_type, wikidb119_image_img_height, wikidb119_image_img_timestamp, wikidb119_image_img_metadata, wikidb119_image_img_user}

# wikidb119_iwlinks class attributes and methods
wikidb119_iwlinks_iwl_prefix: Property = Property(name="iwl_prefix", type=StringType)
wikidb119_iwlinks_iwl_from: Property = Property(name="iwl_from", type=StringType)
wikidb119_iwlinks_iwl_title: Property = Property(name="iwl_title", type=StringType)
wikidb119_iwlinks.attributes={wikidb119_iwlinks_iwl_title, wikidb119_iwlinks_iwl_from, wikidb119_iwlinks_iwl_prefix}

# wikidb119_change_tag class attributes and methods
wikidb119_change_tag_ct_params: Property = Property(name="ct_params", type=StringType)
wikidb119_change_tag_ct_rc_id: Property = Property(name="ct_rc_id", type=StringType)
wikidb119_change_tag_ct_rev_id: Property = Property(name="ct_rev_id", type=StringType)
wikidb119_change_tag_ct_log_id: Property = Property(name="ct_log_id", type=StringType)
wikidb119_change_tag_ct_tag: Property = Property(name="ct_tag", type=StringType)
wikidb119_change_tag.attributes={wikidb119_change_tag_ct_rc_id, wikidb119_change_tag_ct_log_id, wikidb119_change_tag_ct_rev_id, wikidb119_change_tag_ct_params, wikidb119_change_tag_ct_tag}

# wikidb119_valid_tag class attributes and methods
wikidb119_valid_tag_vt_tag: Property = Property(name="vt_tag", type=StringType)
wikidb119_valid_tag.attributes={wikidb119_valid_tag_vt_tag}

# wikidb119_interwiki class attributes and methods
wikidb119_interwiki_iw_trans: Property = Property(name="iw_trans", type=IntegerType)
wikidb119_interwiki_iw_wikiid: Property = Property(name="iw_wikiid", type=StringType)
wikidb119_interwiki_iw_api: Property = Property(name="iw_api", type=StringType)
wikidb119_interwiki_iw_url: Property = Property(name="iw_url", type=StringType)
wikidb119_interwiki_iw_prefix: Property = Property(name="iw_prefix", type=StringType)
wikidb119_interwiki_iw_local: Property = Property(name="iw_local", type=IntegerType)
wikidb119_interwiki.attributes={wikidb119_interwiki_iw_local, wikidb119_interwiki_iw_url, wikidb119_interwiki_iw_prefix, wikidb119_interwiki_iw_wikiid, wikidb119_interwiki_iw_api, wikidb119_interwiki_iw_trans}

# wikidb119_external_user class attributes and methods
wikidb119_external_user_eu_external_id: Property = Property(name="eu_external_id", type=StringType)
wikidb119_external_user_eu_local_id: Property = Property(name="eu_local_id", type=StringType)
wikidb119_external_user.attributes={wikidb119_external_user_eu_local_id, wikidb119_external_user_eu_external_id}

# wikidb119_module_deps class attributes and methods
wikidb119_module_deps_md_skin: Property = Property(name="md_skin", type=StringType)
wikidb119_module_deps_md_deps: Property = Property(name="md_deps", type=StringType)
wikidb119_module_deps_md_module: Property = Property(name="md_module", type=StringType)
wikidb119_module_deps.attributes={wikidb119_module_deps_md_deps, wikidb119_module_deps_md_skin, wikidb119_module_deps_md_module}

# wikidb119_querycache class attributes and methods
wikidb119_querycache_qc_value: Property = Property(name="qc_value", type=StringType)
wikidb119_querycache_qc_type: Property = Property(name="qc_type", type=StringType)
wikidb119_querycache_qc_namespace: Property = Property(name="qc_namespace", type=StringType)
wikidb119_querycache_qc_title: Property = Property(name="qc_title", type=StringType)
wikidb119_querycache.attributes={wikidb119_querycache_qc_title, wikidb119_querycache_qc_value, wikidb119_querycache_qc_namespace, wikidb119_querycache_qc_type}

# wikidb119_logging class attributes and methods
wikidb119_logging_log_params: Property = Property(name="log_params", type=StringType)
wikidb119_logging_log_namespace: Property = Property(name="log_namespace", type=StringType)
wikidb119_logging_log_action: Property = Property(name="log_action", type=StringType)
wikidb119_logging_log_timestamp: Property = Property(name="log_timestamp", type=StringType)
wikidb119_logging_log_page: Property = Property(name="log_page", type=StringType)
wikidb119_logging_log_title: Property = Property(name="log_title", type=StringType)
wikidb119_logging_log_user: Property = Property(name="log_user", type=StringType)
wikidb119_logging_log_deleted: Property = Property(name="log_deleted", type=IntegerType)
wikidb119_logging_log_user_text: Property = Property(name="log_user_text", type=StringType)
wikidb119_logging_log_type: Property = Property(name="log_type", type=StringType)
wikidb119_logging_log_id: Property = Property(name="log_id", type=StringType)
wikidb119_logging_log_comment: Property = Property(name="log_comment", type=StringType)
wikidb119_logging.attributes={wikidb119_logging_log_namespace, wikidb119_logging_log_params, wikidb119_logging_log_title, wikidb119_logging_log_type, wikidb119_logging_log_comment, wikidb119_logging_log_action, wikidb119_logging_log_user_text, wikidb119_logging_log_page, wikidb119_logging_log_timestamp, wikidb119_logging_log_user, wikidb119_logging_log_deleted, wikidb119_logging_log_id}

# wikidb119_tag_summary class attributes and methods
wikidb119_tag_summary_ts_log_id: Property = Property(name="ts_log_id", type=StringType)
wikidb119_tag_summary_ts_tags: Property = Property(name="ts_tags", type=StringType)
wikidb119_tag_summary_ts_rc_id: Property = Property(name="ts_rc_id", type=StringType)
wikidb119_tag_summary_ts_rev_id: Property = Property(name="ts_rev_id", type=StringType)
wikidb119_tag_summary.attributes={wikidb119_tag_summary_ts_log_id, wikidb119_tag_summary_ts_tags, wikidb119_tag_summary_ts_rev_id, wikidb119_tag_summary_ts_rc_id}

# wikidb119_objectcache class attributes and methods
wikidb119_objectcache_exptime: Property = Property(name="exptime", type=DateType)
wikidb119_objectcache_value: Property = Property(name="value", type=StringType)
wikidb119_objectcache_keyname: Property = Property(name="keyname", type=StringType)
wikidb119_objectcache.attributes={wikidb119_objectcache_keyname, wikidb119_objectcache_exptime, wikidb119_objectcache_value}

# wikidb119_protected_titles class attributes and methods
wikidb119_protected_titles_pt_namespace: Property = Property(name="pt_namespace", type=StringType)
wikidb119_protected_titles_pt_expiry: Property = Property(name="pt_expiry", type=StringType)
wikidb119_protected_titles_pt_title: Property = Property(name="pt_title", type=StringType)
wikidb119_protected_titles_pt_create_perm: Property = Property(name="pt_create_perm", type=StringType)
wikidb119_protected_titles_pt_user: Property = Property(name="pt_user", type=StringType)
wikidb119_protected_titles_pt_timestamp: Property = Property(name="pt_timestamp", type=StringType)
wikidb119_protected_titles_pt_reason: Property = Property(name="pt_reason", type=StringType)
wikidb119_protected_titles.attributes={wikidb119_protected_titles_pt_user, wikidb119_protected_titles_pt_expiry, wikidb119_protected_titles_pt_title, wikidb119_protected_titles_pt_timestamp, wikidb119_protected_titles_pt_create_perm, wikidb119_protected_titles_pt_namespace, wikidb119_protected_titles_pt_reason}

# wikidb119_recentchanges class attributes and methods
wikidb119_recentchanges_rc_minor: Property = Property(name="rc_minor", type=IntegerType)
wikidb119_recentchanges_rc_log_type: Property = Property(name="rc_log_type", type=StringType)
wikidb119_recentchanges_rc_id: Property = Property(name="rc_id", type=StringType)
wikidb119_recentchanges_rc_last_oldid: Property = Property(name="rc_last_oldid", type=StringType)
wikidb119_recentchanges_rc_cur_id: Property = Property(name="rc_cur_id", type=StringType)
wikidb119_recentchanges_rc_patrolled: Property = Property(name="rc_patrolled", type=IntegerType)
wikidb119_recentchanges_rc_new: Property = Property(name="rc_new", type=IntegerType)
wikidb119_recentchanges_rc_new_len: Property = Property(name="rc_new_len", type=StringType)
wikidb119_recentchanges_rc_this_oldid: Property = Property(name="rc_this_oldid", type=StringType)
wikidb119_recentchanges_rc_timestamp: Property = Property(name="rc_timestamp", type=StringType)
wikidb119_recentchanges_rc_type: Property = Property(name="rc_type", type=IntegerType)
wikidb119_recentchanges_rc_cur_time: Property = Property(name="rc_cur_time", type=StringType)
wikidb119_recentchanges_rc_bot: Property = Property(name="rc_bot", type=IntegerType)
wikidb119_recentchanges_rc_user_text: Property = Property(name="rc_user_text", type=StringType)
wikidb119_recentchanges_rc_logid: Property = Property(name="rc_logid", type=StringType)
wikidb119_recentchanges_rc_user: Property = Property(name="rc_user", type=StringType)
wikidb119_recentchanges_rc_log_action: Property = Property(name="rc_log_action", type=StringType)
wikidb119_recentchanges_rc_params: Property = Property(name="rc_params", type=StringType)
wikidb119_recentchanges_rc_comment: Property = Property(name="rc_comment", type=StringType)
wikidb119_recentchanges_rc_ip: Property = Property(name="rc_ip", type=StringType)
wikidb119_recentchanges_rc_old_len: Property = Property(name="rc_old_len", type=StringType)
wikidb119_recentchanges_rc_title: Property = Property(name="rc_title", type=StringType)
wikidb119_recentchanges_rc_moved_to_ns: Property = Property(name="rc_moved_to_ns", type=IntegerType)
wikidb119_recentchanges_rc_deleted: Property = Property(name="rc_deleted", type=IntegerType)
wikidb119_recentchanges_rc_namespace: Property = Property(name="rc_namespace", type=StringType)
wikidb119_recentchanges_rc_moved_to_title: Property = Property(name="rc_moved_to_title", type=StringType)
wikidb119_recentchanges.attributes={wikidb119_recentchanges_rc_moved_to_ns, wikidb119_recentchanges_rc_deleted, wikidb119_recentchanges_rc_last_oldid, wikidb119_recentchanges_rc_minor, wikidb119_recentchanges_rc_logid, wikidb119_recentchanges_rc_params, wikidb119_recentchanges_rc_log_action, wikidb119_recentchanges_rc_moved_to_title, wikidb119_recentchanges_rc_user, wikidb119_recentchanges_rc_old_len, wikidb119_recentchanges_rc_this_oldid, wikidb119_recentchanges_rc_bot, wikidb119_recentchanges_rc_log_type, wikidb119_recentchanges_rc_id, wikidb119_recentchanges_rc_cur_time, wikidb119_recentchanges_rc_type, wikidb119_recentchanges_rc_patrolled, wikidb119_recentchanges_rc_namespace, wikidb119_recentchanges_rc_user_text, wikidb119_recentchanges_rc_new_len, wikidb119_recentchanges_rc_title, wikidb119_recentchanges_rc_cur_id, wikidb119_recentchanges_rc_comment, wikidb119_recentchanges_rc_new, wikidb119_recentchanges_rc_ip, wikidb119_recentchanges_rc_timestamp}

# wikidb119_page_restrictions class attributes and methods
wikidb119_page_restrictions_pr_expiry: Property = Property(name="pr_expiry", type=StringType)
wikidb119_page_restrictions_pr_cascade: Property = Property(name="pr_cascade", type=IntegerType)
wikidb119_page_restrictions_pr_id: Property = Property(name="pr_id", type=StringType)
wikidb119_page_restrictions_pr_level: Property = Property(name="pr_level", type=StringType)
wikidb119_page_restrictions_pr_user: Property = Property(name="pr_user", type=StringType)
wikidb119_page_restrictions_pr_type: Property = Property(name="pr_type", type=StringType)
wikidb119_page_restrictions_pr_page: Property = Property(name="pr_page", type=StringType)
wikidb119_page_restrictions.attributes={wikidb119_page_restrictions_pr_type, wikidb119_page_restrictions_pr_expiry, wikidb119_page_restrictions_pr_cascade, wikidb119_page_restrictions_pr_id, wikidb119_page_restrictions_pr_user, wikidb119_page_restrictions_pr_level, wikidb119_page_restrictions_pr_page}

# wikidb119_log_search class attributes and methods
wikidb119_log_search_ls_value: Property = Property(name="ls_value", type=StringType)
wikidb119_log_search_ls_log_id: Property = Property(name="ls_log_id", type=StringType)
wikidb119_log_search_ls_field: Property = Property(name="ls_field", type=StringType)
wikidb119_log_search.attributes={wikidb119_log_search_ls_value, wikidb119_log_search_ls_log_id, wikidb119_log_search_ls_field}

# wikidb119_user_groups class attributes and methods
wikidb119_user_groups_ug_group: Property = Property(name="ug_group", type=StringType)
wikidb119_user_groups_ug_user: Property = Property(name="ug_user", type=StringType)
wikidb119_user_groups.attributes={wikidb119_user_groups_ug_group, wikidb119_user_groups_ug_user}

# wikidb119_user_newtalk class attributes and methods
wikidb119_user_newtalk_user_last_timestamp: Property = Property(name="user_last_timestamp", type=StringType)
wikidb119_user_newtalk_user_id: Property = Property(name="user_id", type=StringType)
wikidb119_user_newtalk_user_ip: Property = Property(name="user_ip", type=StringType)
wikidb119_user_newtalk.attributes={wikidb119_user_newtalk_user_id, wikidb119_user_newtalk_user_last_timestamp, wikidb119_user_newtalk_user_ip}

# wikidb119_filearchive class attributes and methods
wikidb119_filearchive_fa_storage_key: Property = Property(name="fa_storage_key", type=StringType)
wikidb119_filearchive_fa_bits: Property = Property(name="fa_bits", type=StringType)
wikidb119_filearchive_fa_id: Property = Property(name="fa_id", type=StringType)
wikidb119_filearchive_fa_size: Property = Property(name="fa_size", type=StringType)
wikidb119_filearchive_fa_deleted: Property = Property(name="fa_deleted", type=IntegerType)
wikidb119_filearchive_fa_metadata: Property = Property(name="fa_metadata", type=StringType)
wikidb119_filearchive_fa_description: Property = Property(name="fa_description", type=StringType)
wikidb119_filearchive_fa_deleted_reason: Property = Property(name="fa_deleted_reason", type=StringType)
wikidb119_filearchive_fa_media_type: Property = Property(name="fa_media_type", type=StringType)
wikidb119_filearchive_fa_user_text: Property = Property(name="fa_user_text", type=StringType)
wikidb119_filearchive_fa_major_mime: Property = Property(name="fa_major_mime", type=StringType)
wikidb119_filearchive_fa_deleted_timestamp: Property = Property(name="fa_deleted_timestamp", type=StringType)
wikidb119_filearchive_fa_width: Property = Property(name="fa_width", type=StringType)
wikidb119_filearchive_fa_height: Property = Property(name="fa_height", type=StringType)
wikidb119_filearchive_fa_minor_mime: Property = Property(name="fa_minor_mime", type=StringType)
wikidb119_filearchive_fa_storage_group: Property = Property(name="fa_storage_group", type=StringType)
wikidb119_filearchive_fa_archive_name: Property = Property(name="fa_archive_name", type=StringType)
wikidb119_filearchive_fa_name: Property = Property(name="fa_name", type=StringType)
wikidb119_filearchive_fa_user: Property = Property(name="fa_user", type=StringType)
wikidb119_filearchive_fa_timestamp: Property = Property(name="fa_timestamp", type=StringType)
wikidb119_filearchive_fa_deleted_user: Property = Property(name="fa_deleted_user", type=StringType)
wikidb119_filearchive.attributes={wikidb119_filearchive_fa_user, wikidb119_filearchive_fa_id, wikidb119_filearchive_fa_height, wikidb119_filearchive_fa_major_mime, wikidb119_filearchive_fa_deleted_reason, wikidb119_filearchive_fa_archive_name, wikidb119_filearchive_fa_deleted_timestamp, wikidb119_filearchive_fa_storage_group, wikidb119_filearchive_fa_size, wikidb119_filearchive_fa_user_text, wikidb119_filearchive_fa_bits, wikidb119_filearchive_fa_media_type, wikidb119_filearchive_fa_metadata, wikidb119_filearchive_fa_deleted_user, wikidb119_filearchive_fa_name, wikidb119_filearchive_fa_deleted, wikidb119_filearchive_fa_description, wikidb119_filearchive_fa_width, wikidb119_filearchive_fa_storage_key, wikidb119_filearchive_fa_minor_mime, wikidb119_filearchive_fa_timestamp}

# wikidb119_ipblocks class attributes and methods
wikidb119_ipblocks_ipb_auto: Property = Property(name="ipb_auto", type=IntegerType)
wikidb119_ipblocks_ipb_create_account: Property = Property(name="ipb_create_account", type=IntegerType)
wikidb119_ipblocks_ipb_anon_only: Property = Property(name="ipb_anon_only", type=IntegerType)
wikidb119_ipblocks_ipb_block_email: Property = Property(name="ipb_block_email", type=IntegerType)
wikidb119_ipblocks_ipb_id: Property = Property(name="ipb_id", type=StringType)
wikidb119_ipblocks_ipb_reason: Property = Property(name="ipb_reason", type=StringType)
wikidb119_ipblocks_ipb_timestamp: Property = Property(name="ipb_timestamp", type=StringType)
wikidb119_ipblocks_ipb_range_end: Property = Property(name="ipb_range_end", type=StringType)
wikidb119_ipblocks_ipb_allow_usertalk: Property = Property(name="ipb_allow_usertalk", type=IntegerType)
wikidb119_ipblocks_ipb_range_start: Property = Property(name="ipb_range_start", type=StringType)
wikidb119_ipblocks_ipb_expiry: Property = Property(name="ipb_expiry", type=StringType)
wikidb119_ipblocks_ipb_deleted: Property = Property(name="ipb_deleted", type=IntegerType)
wikidb119_ipblocks_ipb_user: Property = Property(name="ipb_user", type=StringType)
wikidb119_ipblocks_ipb_by: Property = Property(name="ipb_by", type=StringType)
wikidb119_ipblocks_ipb_by_text: Property = Property(name="ipb_by_text", type=StringType)
wikidb119_ipblocks_ipb_enable_autoblock: Property = Property(name="ipb_enable_autoblock", type=IntegerType)
wikidb119_ipblocks_ipb_address: Property = Property(name="ipb_address", type=StringType)
wikidb119_ipblocks.attributes={wikidb119_ipblocks_ipb_user, wikidb119_ipblocks_ipb_by_text, wikidb119_ipblocks_ipb_range_start, wikidb119_ipblocks_ipb_auto, wikidb119_ipblocks_ipb_deleted, wikidb119_ipblocks_ipb_reason, wikidb119_ipblocks_ipb_create_account, wikidb119_ipblocks_ipb_address, wikidb119_ipblocks_ipb_range_end, wikidb119_ipblocks_ipb_anon_only, wikidb119_ipblocks_ipb_timestamp, wikidb119_ipblocks_ipb_expiry, wikidb119_ipblocks_ipb_by, wikidb119_ipblocks_ipb_id, wikidb119_ipblocks_ipb_block_email, wikidb119_ipblocks_ipb_allow_usertalk, wikidb119_ipblocks_ipb_enable_autoblock}

# wikidb119_hitcounter class attributes and methods
wikidb119_hitcounter_hc_id: Property = Property(name="hc_id", type=StringType)
wikidb119_hitcounter.attributes={wikidb119_hitcounter_hc_id}

# wikidb119_l10n_cache class attributes and methods
wikidb119_l10n_cache_lc_lang: Property = Property(name="lc_lang", type=StringType)
wikidb119_l10n_cache_lc_key: Property = Property(name="lc_key", type=StringType)
wikidb119_l10n_cache_lc_value: Property = Property(name="lc_value", type=StringType)
wikidb119_l10n_cache.attributes={wikidb119_l10n_cache_lc_value, wikidb119_l10n_cache_lc_key, wikidb119_l10n_cache_lc_lang}

# wikidb119_page class attributes and methods
wikidb119_page_page_random: Property = Property(name="page_random", type=FloatType)
wikidb119_page_page_id: Property = Property(name="page_id", type=StringType)
wikidb119_page_page_counter: Property = Property(name="page_counter", type=StringType)
wikidb119_page_page_namespace: Property = Property(name="page_namespace", type=StringType)
wikidb119_page_page_restrictions: Property = Property(name="page_restrictions", type=StringType)
wikidb119_page_page_latest: Property = Property(name="page_latest", type=StringType)
wikidb119_page_page_is_redirect: Property = Property(name="page_is_redirect", type=IntegerType)
wikidb119_page_page_title: Property = Property(name="page_title", type=StringType)
wikidb119_page_page_len: Property = Property(name="page_len", type=StringType)
wikidb119_page_page_touched: Property = Property(name="page_touched", type=StringType)
wikidb119_page_page_is_new: Property = Property(name="page_is_new", type=IntegerType)
wikidb119_page.attributes={wikidb119_page_page_counter, wikidb119_page_page_len, wikidb119_page_page_id, wikidb119_page_page_touched, wikidb119_page_page_random, wikidb119_page_page_restrictions, wikidb119_page_page_latest, wikidb119_page_page_is_redirect, wikidb119_page_page_title, wikidb119_page_page_namespace, wikidb119_page_page_is_new}

# wikidb119_archive class attributes and methods
wikidb119_archive_ar_page_id: Property = Property(name="ar_page_id", type=StringType)
wikidb119_archive_ar_text_id: Property = Property(name="ar_text_id", type=StringType)
wikidb119_archive_ar_timestamp: Property = Property(name="ar_timestamp", type=StringType)
wikidb119_archive_ar_rev_id: Property = Property(name="ar_rev_id", type=StringType)
wikidb119_archive_ar_sha1: Property = Property(name="ar_sha1", type=StringType)
wikidb119_archive_ar_user: Property = Property(name="ar_user", type=StringType)
wikidb119_archive_ar_deleted: Property = Property(name="ar_deleted", type=IntegerType)
wikidb119_archive_ar_namespace: Property = Property(name="ar_namespace", type=StringType)
wikidb119_archive_ar_title: Property = Property(name="ar_title", type=StringType)
wikidb119_archive_ar_text: Property = Property(name="ar_text", type=StringType)
wikidb119_archive_ar_parent_id: Property = Property(name="ar_parent_id", type=StringType)
wikidb119_archive_ar_user_text: Property = Property(name="ar_user_text", type=StringType)
wikidb119_archive_ar_comment: Property = Property(name="ar_comment", type=StringType)
wikidb119_archive_ar_minor_edit: Property = Property(name="ar_minor_edit", type=IntegerType)
wikidb119_archive_ar_flags: Property = Property(name="ar_flags", type=StringType)
wikidb119_archive_ar_len: Property = Property(name="ar_len", type=StringType)
wikidb119_archive.attributes={wikidb119_archive_ar_flags, wikidb119_archive_ar_rev_id, wikidb119_archive_ar_page_id, wikidb119_archive_ar_comment, wikidb119_archive_ar_title, wikidb119_archive_ar_text, wikidb119_archive_ar_namespace, wikidb119_archive_ar_user_text, wikidb119_archive_ar_minor_edit, wikidb119_archive_ar_sha1, wikidb119_archive_ar_user, wikidb119_archive_ar_len, wikidb119_archive_ar_timestamp, wikidb119_archive_ar_parent_id, wikidb119_archive_ar_deleted, wikidb119_archive_ar_text_id}

# wikidb119_oldimage class attributes and methods
wikidb119_oldimage_oi_major_mime: Property = Property(name="oi_major_mime", type=StringType)
wikidb119_oldimage_oi_width: Property = Property(name="oi_width", type=StringType)
wikidb119_oldimage_oi_sha1: Property = Property(name="oi_sha1", type=StringType)
wikidb119_oldimage_oi_description: Property = Property(name="oi_description", type=StringType)
wikidb119_oldimage_oi_size: Property = Property(name="oi_size", type=StringType)
wikidb119_oldimage_oi_name: Property = Property(name="oi_name", type=StringType)
wikidb119_oldimage_oi_timestamp: Property = Property(name="oi_timestamp", type=StringType)
wikidb119_oldimage_oi_minor_mime: Property = Property(name="oi_minor_mime", type=StringType)
wikidb119_oldimage_oi_user_text: Property = Property(name="oi_user_text", type=StringType)
wikidb119_oldimage_oi_archive_name: Property = Property(name="oi_archive_name", type=StringType)
wikidb119_oldimage_oi_media_type: Property = Property(name="oi_media_type", type=StringType)
wikidb119_oldimage_oi_deleted: Property = Property(name="oi_deleted", type=IntegerType)
wikidb119_oldimage_oi_height: Property = Property(name="oi_height", type=StringType)
wikidb119_oldimage_oi_bits: Property = Property(name="oi_bits", type=StringType)
wikidb119_oldimage_oi_metadata: Property = Property(name="oi_metadata", type=StringType)
wikidb119_oldimage_oi_user: Property = Property(name="oi_user", type=StringType)
wikidb119_oldimage.attributes={wikidb119_oldimage_oi_description, wikidb119_oldimage_oi_major_mime, wikidb119_oldimage_oi_deleted, wikidb119_oldimage_oi_media_type, wikidb119_oldimage_oi_timestamp, wikidb119_oldimage_oi_user_text, wikidb119_oldimage_oi_archive_name, wikidb119_oldimage_oi_sha1, wikidb119_oldimage_oi_bits, wikidb119_oldimage_oi_metadata, wikidb119_oldimage_oi_width, wikidb119_oldimage_oi_user, wikidb119_oldimage_oi_name, wikidb119_oldimage_oi_height, wikidb119_oldimage_oi_minor_mime, wikidb119_oldimage_oi_size}

# wikidb119_updatelog class attributes and methods
wikidb119_updatelog_ul_value: Property = Property(name="ul_value", type=StringType)
wikidb119_updatelog_ul_key: Property = Property(name="ul_key", type=StringType)
wikidb119_updatelog.attributes={wikidb119_updatelog_ul_key, wikidb119_updatelog_ul_value}

# wikidb119_user class attributes and methods
wikidb119_user_user_editcount: Property = Property(name="user_editcount", type=StringType)
wikidb119_user_user_email: Property = Property(name="user_email", type=StringType)
wikidb119_user_user_newpassword: Property = Property(name="user_newpassword", type=StringType)
wikidb119_user_user_email_token: Property = Property(name="user_email_token", type=StringType)
wikidb119_user_user_email_token_expires: Property = Property(name="user_email_token_expires", type=StringType)
wikidb119_user_user_name: Property = Property(name="user_name", type=StringType)
wikidb119_user_user_token: Property = Property(name="user_token", type=StringType)
wikidb119_user_user_real_name: Property = Property(name="user_real_name", type=StringType)
wikidb119_user_user_password: Property = Property(name="user_password", type=StringType)
wikidb119_user_user_id: Property = Property(name="user_id", type=StringType)
wikidb119_user_user_registration: Property = Property(name="user_registration", type=StringType)
wikidb119_user_user_touched: Property = Property(name="user_touched", type=StringType)
wikidb119_user_user_email_authenticated: Property = Property(name="user_email_authenticated", type=StringType)
wikidb119_user_user_newpass_time: Property = Property(name="user_newpass_time", type=StringType)
wikidb119_user.attributes={wikidb119_user_user_editcount, wikidb119_user_user_newpassword, wikidb119_user_user_name, wikidb119_user_user_real_name, wikidb119_user_user_email_token_expires, wikidb119_user_user_email, wikidb119_user_user_newpass_time, wikidb119_user_user_touched, wikidb119_user_user_email_authenticated, wikidb119_user_user_registration, wikidb119_user_user_password, wikidb119_user_user_email_token, wikidb119_user_user_id, wikidb119_user_user_token}

# wikidb119_querycache_info class attributes and methods
wikidb119_querycache_info_qci_type: Property = Property(name="qci_type", type=StringType)
wikidb119_querycache_info_qci_timestamp: Property = Property(name="qci_timestamp", type=StringType)
wikidb119_querycache_info.attributes={wikidb119_querycache_info_qci_type, wikidb119_querycache_info_qci_timestamp}

# Domain Model
domain_model = DomainModel(
    name="wikidb119",
    types={wikidb119_site_stats, wikidb119_searchindex, wikidb119_pagelinks, wikidb119_user_properties, wikidb119_revision, wikidb119_user_former_groups, wikidb119_imagelinks, wikidb119_text, wikidb119_watchlist, wikidb119_categorylinks, wikidb119_langlinks, wikidb119_transcache, wikidb119_category, wikidb119_msg_resource, wikidb119_job, wikidb119_querycachetwo, wikidb119_redirect, wikidb119_msg_resource_links, wikidb119_externallinks, wikidb119_page_props, wikidb119_templatelinks, wikidb119_uploadstash, wikidb119_image, wikidb119_iwlinks, wikidb119_change_tag, wikidb119_valid_tag, wikidb119_interwiki, wikidb119_external_user, wikidb119_module_deps, wikidb119_querycache, wikidb119_logging, wikidb119_tag_summary, wikidb119_objectcache, wikidb119_protected_titles, wikidb119_recentchanges, wikidb119_page_restrictions, wikidb119_log_search, wikidb119_user_groups, wikidb119_user_newtalk, wikidb119_filearchive, wikidb119_ipblocks, wikidb119_hitcounter, wikidb119_l10n_cache, wikidb119_page, wikidb119_archive, wikidb119_oldimage, wikidb119_updatelog, wikidb119_user, wikidb119_querycache_info},
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