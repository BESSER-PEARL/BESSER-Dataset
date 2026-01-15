from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class wikidb116_querycache:

    def __init__(self, qc_value: str, qc_type: str, qc_namespace: str, qc_title: str):
        self.qc_value = qc_value
        self.qc_type = qc_type
        self.qc_namespace = qc_namespace
        self.qc_title = qc_title
        
    @property
    def qc_namespace(self) -> str:
        return self.__qc_namespace

    @qc_namespace.setter
    def qc_namespace(self, qc_namespace: str):
        self.__qc_namespace = qc_namespace

    @property
    def qc_title(self) -> str:
        return self.__qc_title

    @qc_title.setter
    def qc_title(self, qc_title: str):
        self.__qc_title = qc_title

    @property
    def qc_type(self) -> str:
        return self.__qc_type

    @qc_type.setter
    def qc_type(self, qc_type: str):
        self.__qc_type = qc_type

    @property
    def qc_value(self) -> str:
        return self.__qc_value

    @qc_value.setter
    def qc_value(self, qc_value: str):
        self.__qc_value = qc_value

class wikidb116_l10n_cache:

    def __init__(self, lc_lang: str, lc_key: str, lc_value: str):
        self.lc_lang = lc_lang
        self.lc_key = lc_key
        self.lc_value = lc_value
        
    @property
    def lc_lang(self) -> str:
        return self.__lc_lang

    @lc_lang.setter
    def lc_lang(self, lc_lang: str):
        self.__lc_lang = lc_lang

    @property
    def lc_value(self) -> str:
        return self.__lc_value

    @lc_value.setter
    def lc_value(self, lc_value: str):
        self.__lc_value = lc_value

    @property
    def lc_key(self) -> str:
        return self.__lc_key

    @lc_key.setter
    def lc_key(self, lc_key: str):
        self.__lc_key = lc_key

class wikidb116_log_search:

    def __init__(self, ls_value: str, ls_log_id: str, ls_field: str):
        self.ls_value = ls_value
        self.ls_log_id = ls_log_id
        self.ls_field = ls_field
        
    @property
    def ls_field(self) -> str:
        return self.__ls_field

    @ls_field.setter
    def ls_field(self, ls_field: str):
        self.__ls_field = ls_field

    @property
    def ls_value(self) -> str:
        return self.__ls_value

    @ls_value.setter
    def ls_value(self, ls_value: str):
        self.__ls_value = ls_value

    @property
    def ls_log_id(self) -> str:
        return self.__ls_log_id

    @ls_log_id.setter
    def ls_log_id(self, ls_log_id: str):
        self.__ls_log_id = ls_log_id

class wikidb116_oldimage:

    def __init__(self, oi_major_mime: str, oi_width: str, oi_sha1: str, oi_description: str, oi_size: str, oi_name: str, oi_timestamp: str, oi_minor_mime: str, oi_user_text: str, oi_height: str, oi_bits: str, oi_metadata: str, oi_user: str, oi_media_type: str, oi_deleted: int, oi_archive_name: str):
        self.oi_major_mime = oi_major_mime
        self.oi_width = oi_width
        self.oi_sha1 = oi_sha1
        self.oi_description = oi_description
        self.oi_size = oi_size
        self.oi_name = oi_name
        self.oi_timestamp = oi_timestamp
        self.oi_minor_mime = oi_minor_mime
        self.oi_user_text = oi_user_text
        self.oi_height = oi_height
        self.oi_bits = oi_bits
        self.oi_metadata = oi_metadata
        self.oi_user = oi_user
        self.oi_media_type = oi_media_type
        self.oi_deleted = oi_deleted
        self.oi_archive_name = oi_archive_name
        
    @property
    def oi_height(self) -> str:
        return self.__oi_height

    @oi_height.setter
    def oi_height(self, oi_height: str):
        self.__oi_height = oi_height

    @property
    def oi_archive_name(self) -> str:
        return self.__oi_archive_name

    @oi_archive_name.setter
    def oi_archive_name(self, oi_archive_name: str):
        self.__oi_archive_name = oi_archive_name

    @property
    def oi_width(self) -> str:
        return self.__oi_width

    @oi_width.setter
    def oi_width(self, oi_width: str):
        self.__oi_width = oi_width

    @property
    def oi_media_type(self) -> str:
        return self.__oi_media_type

    @oi_media_type.setter
    def oi_media_type(self, oi_media_type: str):
        self.__oi_media_type = oi_media_type

    @property
    def oi_name(self) -> str:
        return self.__oi_name

    @oi_name.setter
    def oi_name(self, oi_name: str):
        self.__oi_name = oi_name

    @property
    def oi_sha1(self) -> str:
        return self.__oi_sha1

    @oi_sha1.setter
    def oi_sha1(self, oi_sha1: str):
        self.__oi_sha1 = oi_sha1

    @property
    def oi_deleted(self) -> int:
        return self.__oi_deleted

    @oi_deleted.setter
    def oi_deleted(self, oi_deleted: int):
        self.__oi_deleted = oi_deleted

    @property
    def oi_bits(self) -> str:
        return self.__oi_bits

    @oi_bits.setter
    def oi_bits(self, oi_bits: str):
        self.__oi_bits = oi_bits

    @property
    def oi_major_mime(self) -> str:
        return self.__oi_major_mime

    @oi_major_mime.setter
    def oi_major_mime(self, oi_major_mime: str):
        self.__oi_major_mime = oi_major_mime

    @property
    def oi_minor_mime(self) -> str:
        return self.__oi_minor_mime

    @oi_minor_mime.setter
    def oi_minor_mime(self, oi_minor_mime: str):
        self.__oi_minor_mime = oi_minor_mime

    @property
    def oi_size(self) -> str:
        return self.__oi_size

    @oi_size.setter
    def oi_size(self, oi_size: str):
        self.__oi_size = oi_size

    @property
    def oi_metadata(self) -> str:
        return self.__oi_metadata

    @oi_metadata.setter
    def oi_metadata(self, oi_metadata: str):
        self.__oi_metadata = oi_metadata

    @property
    def oi_user_text(self) -> str:
        return self.__oi_user_text

    @oi_user_text.setter
    def oi_user_text(self, oi_user_text: str):
        self.__oi_user_text = oi_user_text

    @property
    def oi_description(self) -> str:
        return self.__oi_description

    @oi_description.setter
    def oi_description(self, oi_description: str):
        self.__oi_description = oi_description

    @property
    def oi_timestamp(self) -> str:
        return self.__oi_timestamp

    @oi_timestamp.setter
    def oi_timestamp(self, oi_timestamp: str):
        self.__oi_timestamp = oi_timestamp

    @property
    def oi_user(self) -> str:
        return self.__oi_user

    @oi_user.setter
    def oi_user(self, oi_user: str):
        self.__oi_user = oi_user

class wikidb116_change_tag:

    def __init__(self, ct_params: str, ct_rc_id: str, ct_rev_id: str, ct_log_id: str, ct_tag: str):
        self.ct_params = ct_params
        self.ct_rc_id = ct_rc_id
        self.ct_rev_id = ct_rev_id
        self.ct_log_id = ct_log_id
        self.ct_tag = ct_tag
        
    @property
    def ct_params(self) -> str:
        return self.__ct_params

    @ct_params.setter
    def ct_params(self, ct_params: str):
        self.__ct_params = ct_params

    @property
    def ct_rc_id(self) -> str:
        return self.__ct_rc_id

    @ct_rc_id.setter
    def ct_rc_id(self, ct_rc_id: str):
        self.__ct_rc_id = ct_rc_id

    @property
    def ct_tag(self) -> str:
        return self.__ct_tag

    @ct_tag.setter
    def ct_tag(self, ct_tag: str):
        self.__ct_tag = ct_tag

    @property
    def ct_log_id(self) -> str:
        return self.__ct_log_id

    @ct_log_id.setter
    def ct_log_id(self, ct_log_id: str):
        self.__ct_log_id = ct_log_id

    @property
    def ct_rev_id(self) -> str:
        return self.__ct_rev_id

    @ct_rev_id.setter
    def ct_rev_id(self, ct_rev_id: str):
        self.__ct_rev_id = ct_rev_id

class wikidb116_transcache:

    def __init__(self, tc_time: str, tc_url: str, tc_contents: str):
        self.tc_time = tc_time
        self.tc_url = tc_url
        self.tc_contents = tc_contents
        
    @property
    def tc_time(self) -> str:
        return self.__tc_time

    @tc_time.setter
    def tc_time(self, tc_time: str):
        self.__tc_time = tc_time

    @property
    def tc_url(self) -> str:
        return self.__tc_url

    @tc_url.setter
    def tc_url(self, tc_url: str):
        self.__tc_url = tc_url

    @property
    def tc_contents(self) -> str:
        return self.__tc_contents

    @tc_contents.setter
    def tc_contents(self, tc_contents: str):
        self.__tc_contents = tc_contents

class wikidb116_user_newtalk:

    def __init__(self, user_last_timestamp: str, user_id: str, user_ip: str):
        self.user_last_timestamp = user_last_timestamp
        self.user_id = user_id
        self.user_ip = user_ip
        
    @property
    def user_ip(self) -> str:
        return self.__user_ip

    @user_ip.setter
    def user_ip(self, user_ip: str):
        self.__user_ip = user_ip

    @property
    def user_last_timestamp(self) -> str:
        return self.__user_last_timestamp

    @user_last_timestamp.setter
    def user_last_timestamp(self, user_last_timestamp: str):
        self.__user_last_timestamp = user_last_timestamp

    @property
    def user_id(self) -> str:
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self.__user_id = user_id

class wikidb116_valid_tag:

    def __init__(self, vt_tag: str):
        self.vt_tag = vt_tag
        
    @property
    def vt_tag(self) -> str:
        return self.__vt_tag

    @vt_tag.setter
    def vt_tag(self, vt_tag: str):
        self.__vt_tag = vt_tag

class wikidb116_user_properties:

    def __init__(self, up_property: str, up_value: str, up_user: str):
        self.up_property = up_property
        self.up_value = up_value
        self.up_user = up_user
        
    @property
    def up_user(self) -> str:
        return self.__up_user

    @up_user.setter
    def up_user(self, up_user: str):
        self.__up_user = up_user

    @property
    def up_property(self) -> str:
        return self.__up_property

    @up_property.setter
    def up_property(self, up_property: str):
        self.__up_property = up_property

    @property
    def up_value(self) -> str:
        return self.__up_value

    @up_value.setter
    def up_value(self, up_value: str):
        self.__up_value = up_value

class wikidb116_text:

    def __init__(self, old_flags: str, old_text: str, old_id: str):
        self.old_flags = old_flags
        self.old_text = old_text
        self.old_id = old_id
        
    @property
    def old_text(self) -> str:
        return self.__old_text

    @old_text.setter
    def old_text(self, old_text: str):
        self.__old_text = old_text

    @property
    def old_id(self) -> str:
        return self.__old_id

    @old_id.setter
    def old_id(self, old_id: str):
        self.__old_id = old_id

    @property
    def old_flags(self) -> str:
        return self.__old_flags

    @old_flags.setter
    def old_flags(self, old_flags: str):
        self.__old_flags = old_flags

class wikidb116_logging:

    def __init__(self, log_params: str, log_namespace: str, log_action: str, log_timestamp: str, log_page: str, log_title: str, log_user: str, log_deleted: int, log_user_text: str, log_type: str, log_id: str, log_comment: str):
        self.log_params = log_params
        self.log_namespace = log_namespace
        self.log_action = log_action
        self.log_timestamp = log_timestamp
        self.log_page = log_page
        self.log_title = log_title
        self.log_user = log_user
        self.log_deleted = log_deleted
        self.log_user_text = log_user_text
        self.log_type = log_type
        self.log_id = log_id
        self.log_comment = log_comment
        
    @property
    def log_user_text(self) -> str:
        return self.__log_user_text

    @log_user_text.setter
    def log_user_text(self, log_user_text: str):
        self.__log_user_text = log_user_text

    @property
    def log_params(self) -> str:
        return self.__log_params

    @log_params.setter
    def log_params(self, log_params: str):
        self.__log_params = log_params

    @property
    def log_deleted(self) -> int:
        return self.__log_deleted

    @log_deleted.setter
    def log_deleted(self, log_deleted: int):
        self.__log_deleted = log_deleted

    @property
    def log_user(self) -> str:
        return self.__log_user

    @log_user.setter
    def log_user(self, log_user: str):
        self.__log_user = log_user

    @property
    def log_id(self) -> str:
        return self.__log_id

    @log_id.setter
    def log_id(self, log_id: str):
        self.__log_id = log_id

    @property
    def log_title(self) -> str:
        return self.__log_title

    @log_title.setter
    def log_title(self, log_title: str):
        self.__log_title = log_title

    @property
    def log_type(self) -> str:
        return self.__log_type

    @log_type.setter
    def log_type(self, log_type: str):
        self.__log_type = log_type

    @property
    def log_namespace(self) -> str:
        return self.__log_namespace

    @log_namespace.setter
    def log_namespace(self, log_namespace: str):
        self.__log_namespace = log_namespace

    @property
    def log_page(self) -> str:
        return self.__log_page

    @log_page.setter
    def log_page(self, log_page: str):
        self.__log_page = log_page

    @property
    def log_comment(self) -> str:
        return self.__log_comment

    @log_comment.setter
    def log_comment(self, log_comment: str):
        self.__log_comment = log_comment

    @property
    def log_timestamp(self) -> str:
        return self.__log_timestamp

    @log_timestamp.setter
    def log_timestamp(self, log_timestamp: str):
        self.__log_timestamp = log_timestamp

    @property
    def log_action(self) -> str:
        return self.__log_action

    @log_action.setter
    def log_action(self, log_action: str):
        self.__log_action = log_action

class wikidb116_page_props:

    def __init__(self, pp_page: str, pp_value: str, pp_propname: str):
        self.pp_page = pp_page
        self.pp_value = pp_value
        self.pp_propname = pp_propname
        
    @property
    def pp_value(self) -> str:
        return self.__pp_value

    @pp_value.setter
    def pp_value(self, pp_value: str):
        self.__pp_value = pp_value

    @property
    def pp_page(self) -> str:
        return self.__pp_page

    @pp_page.setter
    def pp_page(self, pp_page: str):
        self.__pp_page = pp_page

    @property
    def pp_propname(self) -> str:
        return self.__pp_propname

    @pp_propname.setter
    def pp_propname(self, pp_propname: str):
        self.__pp_propname = pp_propname

class wikidb116_redirect:

    def __init__(self, rd_fragment: str, rd_namespace: str, rd_from: str, rd_title: str, rd_interwiki: str):
        self.rd_fragment = rd_fragment
        self.rd_namespace = rd_namespace
        self.rd_from = rd_from
        self.rd_title = rd_title
        self.rd_interwiki = rd_interwiki
        
    @property
    def rd_title(self) -> str:
        return self.__rd_title

    @rd_title.setter
    def rd_title(self, rd_title: str):
        self.__rd_title = rd_title

    @property
    def rd_from(self) -> str:
        return self.__rd_from

    @rd_from.setter
    def rd_from(self, rd_from: str):
        self.__rd_from = rd_from

    @property
    def rd_fragment(self) -> str:
        return self.__rd_fragment

    @rd_fragment.setter
    def rd_fragment(self, rd_fragment: str):
        self.__rd_fragment = rd_fragment

    @property
    def rd_namespace(self) -> str:
        return self.__rd_namespace

    @rd_namespace.setter
    def rd_namespace(self, rd_namespace: str):
        self.__rd_namespace = rd_namespace

    @property
    def rd_interwiki(self) -> str:
        return self.__rd_interwiki

    @rd_interwiki.setter
    def rd_interwiki(self, rd_interwiki: str):
        self.__rd_interwiki = rd_interwiki

class wikidb116_tag_summary:

    def __init__(self, ts_log_id: str, ts_tags: str, ts_rc_id: str, ts_rev_id: str):
        self.ts_log_id = ts_log_id
        self.ts_tags = ts_tags
        self.ts_rc_id = ts_rc_id
        self.ts_rev_id = ts_rev_id
        
    @property
    def ts_tags(self) -> str:
        return self.__ts_tags

    @ts_tags.setter
    def ts_tags(self, ts_tags: str):
        self.__ts_tags = ts_tags

    @property
    def ts_rev_id(self) -> str:
        return self.__ts_rev_id

    @ts_rev_id.setter
    def ts_rev_id(self, ts_rev_id: str):
        self.__ts_rev_id = ts_rev_id

    @property
    def ts_rc_id(self) -> str:
        return self.__ts_rc_id

    @ts_rc_id.setter
    def ts_rc_id(self, ts_rc_id: str):
        self.__ts_rc_id = ts_rc_id

    @property
    def ts_log_id(self) -> str:
        return self.__ts_log_id

    @ts_log_id.setter
    def ts_log_id(self, ts_log_id: str):
        self.__ts_log_id = ts_log_id

class wikidb116_page:

    def __init__(self, page_len: str, page_touched: str, page_is_new: int, page_random: float, page_id: str, page_counter: str, page_namespace: str, page_restrictions: str, page_latest: str, page_is_redirect: int, page_title: str):
        self.page_len = page_len
        self.page_touched = page_touched
        self.page_is_new = page_is_new
        self.page_random = page_random
        self.page_id = page_id
        self.page_counter = page_counter
        self.page_namespace = page_namespace
        self.page_restrictions = page_restrictions
        self.page_latest = page_latest
        self.page_is_redirect = page_is_redirect
        self.page_title = page_title
        
    @property
    def page_touched(self) -> str:
        return self.__page_touched

    @page_touched.setter
    def page_touched(self, page_touched: str):
        self.__page_touched = page_touched

    @property
    def page_id(self) -> str:
        return self.__page_id

    @page_id.setter
    def page_id(self, page_id: str):
        self.__page_id = page_id

    @property
    def page_is_new(self) -> int:
        return self.__page_is_new

    @page_is_new.setter
    def page_is_new(self, page_is_new: int):
        self.__page_is_new = page_is_new

    @property
    def page_counter(self) -> str:
        return self.__page_counter

    @page_counter.setter
    def page_counter(self, page_counter: str):
        self.__page_counter = page_counter

    @property
    def page_namespace(self) -> str:
        return self.__page_namespace

    @page_namespace.setter
    def page_namespace(self, page_namespace: str):
        self.__page_namespace = page_namespace

    @property
    def page_latest(self) -> str:
        return self.__page_latest

    @page_latest.setter
    def page_latest(self, page_latest: str):
        self.__page_latest = page_latest

    @property
    def page_title(self) -> str:
        return self.__page_title

    @page_title.setter
    def page_title(self, page_title: str):
        self.__page_title = page_title

    @property
    def page_restrictions(self) -> str:
        return self.__page_restrictions

    @page_restrictions.setter
    def page_restrictions(self, page_restrictions: str):
        self.__page_restrictions = page_restrictions

    @property
    def page_len(self) -> str:
        return self.__page_len

    @page_len.setter
    def page_len(self, page_len: str):
        self.__page_len = page_len

    @property
    def page_random(self) -> float:
        return self.__page_random

    @page_random.setter
    def page_random(self, page_random: float):
        self.__page_random = page_random

    @property
    def page_is_redirect(self) -> int:
        return self.__page_is_redirect

    @page_is_redirect.setter
    def page_is_redirect(self, page_is_redirect: int):
        self.__page_is_redirect = page_is_redirect

class wikidb116_pagelinks:

    def __init__(self, pl_from: str, pl_namespace: str, pl_title: str):
        self.pl_from = pl_from
        self.pl_namespace = pl_namespace
        self.pl_title = pl_title
        
    @property
    def pl_from(self) -> str:
        return self.__pl_from

    @pl_from.setter
    def pl_from(self, pl_from: str):
        self.__pl_from = pl_from

    @property
    def pl_namespace(self) -> str:
        return self.__pl_namespace

    @pl_namespace.setter
    def pl_namespace(self, pl_namespace: str):
        self.__pl_namespace = pl_namespace

    @property
    def pl_title(self) -> str:
        return self.__pl_title

    @pl_title.setter
    def pl_title(self, pl_title: str):
        self.__pl_title = pl_title

class wikidb116_external_user:

    def __init__(self, eu_external_id: str, eu_local_id: str):
        self.eu_external_id = eu_external_id
        self.eu_local_id = eu_local_id
        
    @property
    def eu_external_id(self) -> str:
        return self.__eu_external_id

    @eu_external_id.setter
    def eu_external_id(self, eu_external_id: str):
        self.__eu_external_id = eu_external_id

    @property
    def eu_local_id(self) -> str:
        return self.__eu_local_id

    @eu_local_id.setter
    def eu_local_id(self, eu_local_id: str):
        self.__eu_local_id = eu_local_id

class wikidb116_site_stats:

    def __init__(self, ss_active_users: str, ss_users: str, ss_total_views: str, ss_images: str, ss_total_pages: str, ss_total_edits: str, ss_good_articles: str, ss_admins: str, ss_row_id: str):
        self.ss_active_users = ss_active_users
        self.ss_users = ss_users
        self.ss_total_views = ss_total_views
        self.ss_images = ss_images
        self.ss_total_pages = ss_total_pages
        self.ss_total_edits = ss_total_edits
        self.ss_good_articles = ss_good_articles
        self.ss_admins = ss_admins
        self.ss_row_id = ss_row_id
        
    @property
    def ss_row_id(self) -> str:
        return self.__ss_row_id

    @ss_row_id.setter
    def ss_row_id(self, ss_row_id: str):
        self.__ss_row_id = ss_row_id

    @property
    def ss_total_pages(self) -> str:
        return self.__ss_total_pages

    @ss_total_pages.setter
    def ss_total_pages(self, ss_total_pages: str):
        self.__ss_total_pages = ss_total_pages

    @property
    def ss_admins(self) -> str:
        return self.__ss_admins

    @ss_admins.setter
    def ss_admins(self, ss_admins: str):
        self.__ss_admins = ss_admins

    @property
    def ss_total_views(self) -> str:
        return self.__ss_total_views

    @ss_total_views.setter
    def ss_total_views(self, ss_total_views: str):
        self.__ss_total_views = ss_total_views

    @property
    def ss_good_articles(self) -> str:
        return self.__ss_good_articles

    @ss_good_articles.setter
    def ss_good_articles(self, ss_good_articles: str):
        self.__ss_good_articles = ss_good_articles

    @property
    def ss_total_edits(self) -> str:
        return self.__ss_total_edits

    @ss_total_edits.setter
    def ss_total_edits(self, ss_total_edits: str):
        self.__ss_total_edits = ss_total_edits

    @property
    def ss_active_users(self) -> str:
        return self.__ss_active_users

    @ss_active_users.setter
    def ss_active_users(self, ss_active_users: str):
        self.__ss_active_users = ss_active_users

    @property
    def ss_images(self) -> str:
        return self.__ss_images

    @ss_images.setter
    def ss_images(self, ss_images: str):
        self.__ss_images = ss_images

    @property
    def ss_users(self) -> str:
        return self.__ss_users

    @ss_users.setter
    def ss_users(self, ss_users: str):
        self.__ss_users = ss_users

class wikidb116_ipblocks:

    def __init__(self, ipb_auto: int, ipb_create_account: int, ipb_anon_only: int, ipb_block_email: int, ipb_by_text: str, ipb_enable_autoblock: int, ipb_reason: str, ipb_timestamp: str, ipb_range_end: str, ipb_allow_usertalk: int, ipb_range_start: str, ipb_expiry: str, ipb_deleted: int, ipb_user: str, ipb_by: str, ipb_address: str, ipb_id: str):
        self.ipb_auto = ipb_auto
        self.ipb_create_account = ipb_create_account
        self.ipb_anon_only = ipb_anon_only
        self.ipb_block_email = ipb_block_email
        self.ipb_by_text = ipb_by_text
        self.ipb_enable_autoblock = ipb_enable_autoblock
        self.ipb_reason = ipb_reason
        self.ipb_timestamp = ipb_timestamp
        self.ipb_range_end = ipb_range_end
        self.ipb_allow_usertalk = ipb_allow_usertalk
        self.ipb_range_start = ipb_range_start
        self.ipb_expiry = ipb_expiry
        self.ipb_deleted = ipb_deleted
        self.ipb_user = ipb_user
        self.ipb_by = ipb_by
        self.ipb_address = ipb_address
        self.ipb_id = ipb_id
        
    @property
    def ipb_enable_autoblock(self) -> int:
        return self.__ipb_enable_autoblock

    @ipb_enable_autoblock.setter
    def ipb_enable_autoblock(self, ipb_enable_autoblock: int):
        self.__ipb_enable_autoblock = ipb_enable_autoblock

    @property
    def ipb_range_start(self) -> str:
        return self.__ipb_range_start

    @ipb_range_start.setter
    def ipb_range_start(self, ipb_range_start: str):
        self.__ipb_range_start = ipb_range_start

    @property
    def ipb_expiry(self) -> str:
        return self.__ipb_expiry

    @ipb_expiry.setter
    def ipb_expiry(self, ipb_expiry: str):
        self.__ipb_expiry = ipb_expiry

    @property
    def ipb_timestamp(self) -> str:
        return self.__ipb_timestamp

    @ipb_timestamp.setter
    def ipb_timestamp(self, ipb_timestamp: str):
        self.__ipb_timestamp = ipb_timestamp

    @property
    def ipb_user(self) -> str:
        return self.__ipb_user

    @ipb_user.setter
    def ipb_user(self, ipb_user: str):
        self.__ipb_user = ipb_user

    @property
    def ipb_allow_usertalk(self) -> int:
        return self.__ipb_allow_usertalk

    @ipb_allow_usertalk.setter
    def ipb_allow_usertalk(self, ipb_allow_usertalk: int):
        self.__ipb_allow_usertalk = ipb_allow_usertalk

    @property
    def ipb_anon_only(self) -> int:
        return self.__ipb_anon_only

    @ipb_anon_only.setter
    def ipb_anon_only(self, ipb_anon_only: int):
        self.__ipb_anon_only = ipb_anon_only

    @property
    def ipb_range_end(self) -> str:
        return self.__ipb_range_end

    @ipb_range_end.setter
    def ipb_range_end(self, ipb_range_end: str):
        self.__ipb_range_end = ipb_range_end

    @property
    def ipb_deleted(self) -> int:
        return self.__ipb_deleted

    @ipb_deleted.setter
    def ipb_deleted(self, ipb_deleted: int):
        self.__ipb_deleted = ipb_deleted

    @property
    def ipb_by_text(self) -> str:
        return self.__ipb_by_text

    @ipb_by_text.setter
    def ipb_by_text(self, ipb_by_text: str):
        self.__ipb_by_text = ipb_by_text

    @property
    def ipb_by(self) -> str:
        return self.__ipb_by

    @ipb_by.setter
    def ipb_by(self, ipb_by: str):
        self.__ipb_by = ipb_by

    @property
    def ipb_address(self) -> str:
        return self.__ipb_address

    @ipb_address.setter
    def ipb_address(self, ipb_address: str):
        self.__ipb_address = ipb_address

    @property
    def ipb_auto(self) -> int:
        return self.__ipb_auto

    @ipb_auto.setter
    def ipb_auto(self, ipb_auto: int):
        self.__ipb_auto = ipb_auto

    @property
    def ipb_id(self) -> str:
        return self.__ipb_id

    @ipb_id.setter
    def ipb_id(self, ipb_id: str):
        self.__ipb_id = ipb_id

    @property
    def ipb_create_account(self) -> int:
        return self.__ipb_create_account

    @ipb_create_account.setter
    def ipb_create_account(self, ipb_create_account: int):
        self.__ipb_create_account = ipb_create_account

    @property
    def ipb_block_email(self) -> int:
        return self.__ipb_block_email

    @ipb_block_email.setter
    def ipb_block_email(self, ipb_block_email: int):
        self.__ipb_block_email = ipb_block_email

    @property
    def ipb_reason(self) -> str:
        return self.__ipb_reason

    @ipb_reason.setter
    def ipb_reason(self, ipb_reason: str):
        self.__ipb_reason = ipb_reason

class wikidb116_querycachetwo:

    def __init__(self, qcc_type: str, qcc_namespacetwo: str, qcc_value: str, qcc_titletwo: str, qcc_namespace: str, qcc_title: str):
        self.qcc_type = qcc_type
        self.qcc_namespacetwo = qcc_namespacetwo
        self.qcc_value = qcc_value
        self.qcc_titletwo = qcc_titletwo
        self.qcc_namespace = qcc_namespace
        self.qcc_title = qcc_title
        
    @property
    def qcc_value(self) -> str:
        return self.__qcc_value

    @qcc_value.setter
    def qcc_value(self, qcc_value: str):
        self.__qcc_value = qcc_value

    @property
    def qcc_namespace(self) -> str:
        return self.__qcc_namespace

    @qcc_namespace.setter
    def qcc_namespace(self, qcc_namespace: str):
        self.__qcc_namespace = qcc_namespace

    @property
    def qcc_type(self) -> str:
        return self.__qcc_type

    @qcc_type.setter
    def qcc_type(self, qcc_type: str):
        self.__qcc_type = qcc_type

    @property
    def qcc_title(self) -> str:
        return self.__qcc_title

    @qcc_title.setter
    def qcc_title(self, qcc_title: str):
        self.__qcc_title = qcc_title

    @property
    def qcc_titletwo(self) -> str:
        return self.__qcc_titletwo

    @qcc_titletwo.setter
    def qcc_titletwo(self, qcc_titletwo: str):
        self.__qcc_titletwo = qcc_titletwo

    @property
    def qcc_namespacetwo(self) -> str:
        return self.__qcc_namespacetwo

    @qcc_namespacetwo.setter
    def qcc_namespacetwo(self, qcc_namespacetwo: str):
        self.__qcc_namespacetwo = qcc_namespacetwo

class wikidb116_recentchanges:

    def __init__(self, rc_minor: int, rc_log_type: str, rc_new: int, rc_new_len: str, rc_this_oldid: str, rc_timestamp: str, rc_type: int, rc_cur_time: str, rc_bot: int, rc_user_text: str, rc_logid: str, rc_user: str, rc_log_action: str, rc_title: str, rc_moved_to_ns: int, rc_id: str, rc_last_oldid: str, rc_cur_id: str, rc_patrolled: int, rc_deleted: int, rc_namespace: str, rc_moved_to_title: str, rc_params: str, rc_comment: str, rc_ip: str, rc_old_len: str):
        self.rc_minor = rc_minor
        self.rc_log_type = rc_log_type
        self.rc_new = rc_new
        self.rc_new_len = rc_new_len
        self.rc_this_oldid = rc_this_oldid
        self.rc_timestamp = rc_timestamp
        self.rc_type = rc_type
        self.rc_cur_time = rc_cur_time
        self.rc_bot = rc_bot
        self.rc_user_text = rc_user_text
        self.rc_logid = rc_logid
        self.rc_user = rc_user
        self.rc_log_action = rc_log_action
        self.rc_title = rc_title
        self.rc_moved_to_ns = rc_moved_to_ns
        self.rc_id = rc_id
        self.rc_last_oldid = rc_last_oldid
        self.rc_cur_id = rc_cur_id
        self.rc_patrolled = rc_patrolled
        self.rc_deleted = rc_deleted
        self.rc_namespace = rc_namespace
        self.rc_moved_to_title = rc_moved_to_title
        self.rc_params = rc_params
        self.rc_comment = rc_comment
        self.rc_ip = rc_ip
        self.rc_old_len = rc_old_len
        
    @property
    def rc_this_oldid(self) -> str:
        return self.__rc_this_oldid

    @rc_this_oldid.setter
    def rc_this_oldid(self, rc_this_oldid: str):
        self.__rc_this_oldid = rc_this_oldid

    @property
    def rc_log_action(self) -> str:
        return self.__rc_log_action

    @rc_log_action.setter
    def rc_log_action(self, rc_log_action: str):
        self.__rc_log_action = rc_log_action

    @property
    def rc_comment(self) -> str:
        return self.__rc_comment

    @rc_comment.setter
    def rc_comment(self, rc_comment: str):
        self.__rc_comment = rc_comment

    @property
    def rc_id(self) -> str:
        return self.__rc_id

    @rc_id.setter
    def rc_id(self, rc_id: str):
        self.__rc_id = rc_id

    @property
    def rc_last_oldid(self) -> str:
        return self.__rc_last_oldid

    @rc_last_oldid.setter
    def rc_last_oldid(self, rc_last_oldid: str):
        self.__rc_last_oldid = rc_last_oldid

    @property
    def rc_cur_id(self) -> str:
        return self.__rc_cur_id

    @rc_cur_id.setter
    def rc_cur_id(self, rc_cur_id: str):
        self.__rc_cur_id = rc_cur_id

    @property
    def rc_log_type(self) -> str:
        return self.__rc_log_type

    @rc_log_type.setter
    def rc_log_type(self, rc_log_type: str):
        self.__rc_log_type = rc_log_type

    @property
    def rc_bot(self) -> int:
        return self.__rc_bot

    @rc_bot.setter
    def rc_bot(self, rc_bot: int):
        self.__rc_bot = rc_bot

    @property
    def rc_cur_time(self) -> str:
        return self.__rc_cur_time

    @rc_cur_time.setter
    def rc_cur_time(self, rc_cur_time: str):
        self.__rc_cur_time = rc_cur_time

    @property
    def rc_timestamp(self) -> str:
        return self.__rc_timestamp

    @rc_timestamp.setter
    def rc_timestamp(self, rc_timestamp: str):
        self.__rc_timestamp = rc_timestamp

    @property
    def rc_user_text(self) -> str:
        return self.__rc_user_text

    @rc_user_text.setter
    def rc_user_text(self, rc_user_text: str):
        self.__rc_user_text = rc_user_text

    @property
    def rc_params(self) -> str:
        return self.__rc_params

    @rc_params.setter
    def rc_params(self, rc_params: str):
        self.__rc_params = rc_params

    @property
    def rc_type(self) -> int:
        return self.__rc_type

    @rc_type.setter
    def rc_type(self, rc_type: int):
        self.__rc_type = rc_type

    @property
    def rc_deleted(self) -> int:
        return self.__rc_deleted

    @rc_deleted.setter
    def rc_deleted(self, rc_deleted: int):
        self.__rc_deleted = rc_deleted

    @property
    def rc_new_len(self) -> str:
        return self.__rc_new_len

    @rc_new_len.setter
    def rc_new_len(self, rc_new_len: str):
        self.__rc_new_len = rc_new_len

    @property
    def rc_new(self) -> int:
        return self.__rc_new

    @rc_new.setter
    def rc_new(self, rc_new: int):
        self.__rc_new = rc_new

    @property
    def rc_moved_to_ns(self) -> int:
        return self.__rc_moved_to_ns

    @rc_moved_to_ns.setter
    def rc_moved_to_ns(self, rc_moved_to_ns: int):
        self.__rc_moved_to_ns = rc_moved_to_ns

    @property
    def rc_ip(self) -> str:
        return self.__rc_ip

    @rc_ip.setter
    def rc_ip(self, rc_ip: str):
        self.__rc_ip = rc_ip

    @property
    def rc_moved_to_title(self) -> str:
        return self.__rc_moved_to_title

    @rc_moved_to_title.setter
    def rc_moved_to_title(self, rc_moved_to_title: str):
        self.__rc_moved_to_title = rc_moved_to_title

    @property
    def rc_logid(self) -> str:
        return self.__rc_logid

    @rc_logid.setter
    def rc_logid(self, rc_logid: str):
        self.__rc_logid = rc_logid

    @property
    def rc_title(self) -> str:
        return self.__rc_title

    @rc_title.setter
    def rc_title(self, rc_title: str):
        self.__rc_title = rc_title

    @property
    def rc_namespace(self) -> str:
        return self.__rc_namespace

    @rc_namespace.setter
    def rc_namespace(self, rc_namespace: str):
        self.__rc_namespace = rc_namespace

    @property
    def rc_minor(self) -> int:
        return self.__rc_minor

    @rc_minor.setter
    def rc_minor(self, rc_minor: int):
        self.__rc_minor = rc_minor

    @property
    def rc_patrolled(self) -> int:
        return self.__rc_patrolled

    @rc_patrolled.setter
    def rc_patrolled(self, rc_patrolled: int):
        self.__rc_patrolled = rc_patrolled

    @property
    def rc_old_len(self) -> str:
        return self.__rc_old_len

    @rc_old_len.setter
    def rc_old_len(self, rc_old_len: str):
        self.__rc_old_len = rc_old_len

    @property
    def rc_user(self) -> str:
        return self.__rc_user

    @rc_user.setter
    def rc_user(self, rc_user: str):
        self.__rc_user = rc_user

class wikidb116_langlinks:

    def __init__(self, ll_from: str, ll_title: str, ll_lang: str):
        self.ll_from = ll_from
        self.ll_title = ll_title
        self.ll_lang = ll_lang
        
    @property
    def ll_title(self) -> str:
        return self.__ll_title

    @ll_title.setter
    def ll_title(self, ll_title: str):
        self.__ll_title = ll_title

    @property
    def ll_lang(self) -> str:
        return self.__ll_lang

    @ll_lang.setter
    def ll_lang(self, ll_lang: str):
        self.__ll_lang = ll_lang

    @property
    def ll_from(self) -> str:
        return self.__ll_from

    @ll_from.setter
    def ll_from(self, ll_from: str):
        self.__ll_from = ll_from

class wikidb116_user_groups:

    def __init__(self, ug_user: str, ug_group: str):
        self.ug_user = ug_user
        self.ug_group = ug_group
        
    @property
    def ug_group(self) -> str:
        return self.__ug_group

    @ug_group.setter
    def ug_group(self, ug_group: str):
        self.__ug_group = ug_group

    @property
    def ug_user(self) -> str:
        return self.__ug_user

    @ug_user.setter
    def ug_user(self, ug_user: str):
        self.__ug_user = ug_user

class wikidb116_archive:

    def __init__(self, ar_comment: str, ar_minor_edit: int, ar_flags: str, ar_page_id: str, ar_text_id: str, ar_timestamp: str, ar_rev_id: str, ar_user: str, ar_deleted: int, ar_parent_id: str, ar_user_text: str, ar_len: str, ar_namespace: str, ar_title: str, ar_text: str):
        self.ar_comment = ar_comment
        self.ar_minor_edit = ar_minor_edit
        self.ar_flags = ar_flags
        self.ar_page_id = ar_page_id
        self.ar_text_id = ar_text_id
        self.ar_timestamp = ar_timestamp
        self.ar_rev_id = ar_rev_id
        self.ar_user = ar_user
        self.ar_deleted = ar_deleted
        self.ar_parent_id = ar_parent_id
        self.ar_user_text = ar_user_text
        self.ar_len = ar_len
        self.ar_namespace = ar_namespace
        self.ar_title = ar_title
        self.ar_text = ar_text
        
    @property
    def ar_rev_id(self) -> str:
        return self.__ar_rev_id

    @ar_rev_id.setter
    def ar_rev_id(self, ar_rev_id: str):
        self.__ar_rev_id = ar_rev_id

    @property
    def ar_deleted(self) -> int:
        return self.__ar_deleted

    @ar_deleted.setter
    def ar_deleted(self, ar_deleted: int):
        self.__ar_deleted = ar_deleted

    @property
    def ar_text(self) -> str:
        return self.__ar_text

    @ar_text.setter
    def ar_text(self, ar_text: str):
        self.__ar_text = ar_text

    @property
    def ar_minor_edit(self) -> int:
        return self.__ar_minor_edit

    @ar_minor_edit.setter
    def ar_minor_edit(self, ar_minor_edit: int):
        self.__ar_minor_edit = ar_minor_edit

    @property
    def ar_parent_id(self) -> str:
        return self.__ar_parent_id

    @ar_parent_id.setter
    def ar_parent_id(self, ar_parent_id: str):
        self.__ar_parent_id = ar_parent_id

    @property
    def ar_page_id(self) -> str:
        return self.__ar_page_id

    @ar_page_id.setter
    def ar_page_id(self, ar_page_id: str):
        self.__ar_page_id = ar_page_id

    @property
    def ar_title(self) -> str:
        return self.__ar_title

    @ar_title.setter
    def ar_title(self, ar_title: str):
        self.__ar_title = ar_title

    @property
    def ar_text_id(self) -> str:
        return self.__ar_text_id

    @ar_text_id.setter
    def ar_text_id(self, ar_text_id: str):
        self.__ar_text_id = ar_text_id

    @property
    def ar_flags(self) -> str:
        return self.__ar_flags

    @ar_flags.setter
    def ar_flags(self, ar_flags: str):
        self.__ar_flags = ar_flags

    @property
    def ar_timestamp(self) -> str:
        return self.__ar_timestamp

    @ar_timestamp.setter
    def ar_timestamp(self, ar_timestamp: str):
        self.__ar_timestamp = ar_timestamp

    @property
    def ar_len(self) -> str:
        return self.__ar_len

    @ar_len.setter
    def ar_len(self, ar_len: str):
        self.__ar_len = ar_len

    @property
    def ar_comment(self) -> str:
        return self.__ar_comment

    @ar_comment.setter
    def ar_comment(self, ar_comment: str):
        self.__ar_comment = ar_comment

    @property
    def ar_user(self) -> str:
        return self.__ar_user

    @ar_user.setter
    def ar_user(self, ar_user: str):
        self.__ar_user = ar_user

    @property
    def ar_namespace(self) -> str:
        return self.__ar_namespace

    @ar_namespace.setter
    def ar_namespace(self, ar_namespace: str):
        self.__ar_namespace = ar_namespace

    @property
    def ar_user_text(self) -> str:
        return self.__ar_user_text

    @ar_user_text.setter
    def ar_user_text(self, ar_user_text: str):
        self.__ar_user_text = ar_user_text

class wikidb116_updatelog:

    def __init__(self, ul_key: str):
        self.ul_key = ul_key
        
    @property
    def ul_key(self) -> str:
        return self.__ul_key

    @ul_key.setter
    def ul_key(self, ul_key: str):
        self.__ul_key = ul_key

class wikidb116_searchindex:

    def __init__(self, si_page: str, si_text: str, si_title: str):
        self.si_page = si_page
        self.si_text = si_text
        self.si_title = si_title
        
    @property
    def si_page(self) -> str:
        return self.__si_page

    @si_page.setter
    def si_page(self, si_page: str):
        self.__si_page = si_page

    @property
    def si_text(self) -> str:
        return self.__si_text

    @si_text.setter
    def si_text(self, si_text: str):
        self.__si_text = si_text

    @property
    def si_title(self) -> str:
        return self.__si_title

    @si_title.setter
    def si_title(self, si_title: str):
        self.__si_title = si_title

class wikidb116_externallinks:

    def __init__(self, el_index: str, el_from: str, el_to: str):
        self.el_index = el_index
        self.el_from = el_from
        self.el_to = el_to
        
    @property
    def el_from(self) -> str:
        return self.__el_from

    @el_from.setter
    def el_from(self, el_from: str):
        self.__el_from = el_from

    @property
    def el_to(self) -> str:
        return self.__el_to

    @el_to.setter
    def el_to(self, el_to: str):
        self.__el_to = el_to

    @property
    def el_index(self) -> str:
        return self.__el_index

    @el_index.setter
    def el_index(self, el_index: str):
        self.__el_index = el_index

class wikidb116_category:

    def __init__(self, cat_id: str, cat_title: str, cat_files: str, cat_hidden: int, cat_subcats: str, cat_pages: str):
        self.cat_id = cat_id
        self.cat_title = cat_title
        self.cat_files = cat_files
        self.cat_hidden = cat_hidden
        self.cat_subcats = cat_subcats
        self.cat_pages = cat_pages
        
    @property
    def cat_title(self) -> str:
        return self.__cat_title

    @cat_title.setter
    def cat_title(self, cat_title: str):
        self.__cat_title = cat_title

    @property
    def cat_subcats(self) -> str:
        return self.__cat_subcats

    @cat_subcats.setter
    def cat_subcats(self, cat_subcats: str):
        self.__cat_subcats = cat_subcats

    @property
    def cat_id(self) -> str:
        return self.__cat_id

    @cat_id.setter
    def cat_id(self, cat_id: str):
        self.__cat_id = cat_id

    @property
    def cat_files(self) -> str:
        return self.__cat_files

    @cat_files.setter
    def cat_files(self, cat_files: str):
        self.__cat_files = cat_files

    @property
    def cat_pages(self) -> str:
        return self.__cat_pages

    @cat_pages.setter
    def cat_pages(self, cat_pages: str):
        self.__cat_pages = cat_pages

    @property
    def cat_hidden(self) -> int:
        return self.__cat_hidden

    @cat_hidden.setter
    def cat_hidden(self, cat_hidden: int):
        self.__cat_hidden = cat_hidden

class wikidb116_revision:

    def __init__(self, rev_user_text: str, rev_page: str, rev_text_id: str, rev_parent_id: str, rev_deleted: int, rev_timestamp: str, rev_len: str, rev_minor_edit: int, rev_comment: str, rev_user: str, rev_id: str):
        self.rev_user_text = rev_user_text
        self.rev_page = rev_page
        self.rev_text_id = rev_text_id
        self.rev_parent_id = rev_parent_id
        self.rev_deleted = rev_deleted
        self.rev_timestamp = rev_timestamp
        self.rev_len = rev_len
        self.rev_minor_edit = rev_minor_edit
        self.rev_comment = rev_comment
        self.rev_user = rev_user
        self.rev_id = rev_id
        
    @property
    def rev_id(self) -> str:
        return self.__rev_id

    @rev_id.setter
    def rev_id(self, rev_id: str):
        self.__rev_id = rev_id

    @property
    def rev_user_text(self) -> str:
        return self.__rev_user_text

    @rev_user_text.setter
    def rev_user_text(self, rev_user_text: str):
        self.__rev_user_text = rev_user_text

    @property
    def rev_minor_edit(self) -> int:
        return self.__rev_minor_edit

    @rev_minor_edit.setter
    def rev_minor_edit(self, rev_minor_edit: int):
        self.__rev_minor_edit = rev_minor_edit

    @property
    def rev_text_id(self) -> str:
        return self.__rev_text_id

    @rev_text_id.setter
    def rev_text_id(self, rev_text_id: str):
        self.__rev_text_id = rev_text_id

    @property
    def rev_timestamp(self) -> str:
        return self.__rev_timestamp

    @rev_timestamp.setter
    def rev_timestamp(self, rev_timestamp: str):
        self.__rev_timestamp = rev_timestamp

    @property
    def rev_comment(self) -> str:
        return self.__rev_comment

    @rev_comment.setter
    def rev_comment(self, rev_comment: str):
        self.__rev_comment = rev_comment

    @property
    def rev_user(self) -> str:
        return self.__rev_user

    @rev_user.setter
    def rev_user(self, rev_user: str):
        self.__rev_user = rev_user

    @property
    def rev_len(self) -> str:
        return self.__rev_len

    @rev_len.setter
    def rev_len(self, rev_len: str):
        self.__rev_len = rev_len

    @property
    def rev_page(self) -> str:
        return self.__rev_page

    @rev_page.setter
    def rev_page(self, rev_page: str):
        self.__rev_page = rev_page

    @property
    def rev_parent_id(self) -> str:
        return self.__rev_parent_id

    @rev_parent_id.setter
    def rev_parent_id(self, rev_parent_id: str):
        self.__rev_parent_id = rev_parent_id

    @property
    def rev_deleted(self) -> int:
        return self.__rev_deleted

    @rev_deleted.setter
    def rev_deleted(self, rev_deleted: int):
        self.__rev_deleted = rev_deleted

class wikidb116_imagelinks:

    def __init__(self, il_from: str, il_to: str):
        self.il_from = il_from
        self.il_to = il_to
        
    @property
    def il_to(self) -> str:
        return self.__il_to

    @il_to.setter
    def il_to(self, il_to: str):
        self.__il_to = il_to

    @property
    def il_from(self) -> str:
        return self.__il_from

    @il_from.setter
    def il_from(self, il_from: str):
        self.__il_from = il_from

class wikidb116_image:

    def __init__(self, img_user: str, img_bits: str, img_minor_mime: str, img_description: str, img_height: str, img_major_mime: str, img_size: str, img_metadata: str, img_media_type: str, img_timestamp: str, img_user_text: str, img_width: str, img_sha1: str, img_name: str):
        self.img_user = img_user
        self.img_bits = img_bits
        self.img_minor_mime = img_minor_mime
        self.img_description = img_description
        self.img_height = img_height
        self.img_major_mime = img_major_mime
        self.img_size = img_size
        self.img_metadata = img_metadata
        self.img_media_type = img_media_type
        self.img_timestamp = img_timestamp
        self.img_user_text = img_user_text
        self.img_width = img_width
        self.img_sha1 = img_sha1
        self.img_name = img_name
        
    @property
    def img_bits(self) -> str:
        return self.__img_bits

    @img_bits.setter
    def img_bits(self, img_bits: str):
        self.__img_bits = img_bits

    @property
    def img_description(self) -> str:
        return self.__img_description

    @img_description.setter
    def img_description(self, img_description: str):
        self.__img_description = img_description

    @property
    def img_timestamp(self) -> str:
        return self.__img_timestamp

    @img_timestamp.setter
    def img_timestamp(self, img_timestamp: str):
        self.__img_timestamp = img_timestamp

    @property
    def img_major_mime(self) -> str:
        return self.__img_major_mime

    @img_major_mime.setter
    def img_major_mime(self, img_major_mime: str):
        self.__img_major_mime = img_major_mime

    @property
    def img_media_type(self) -> str:
        return self.__img_media_type

    @img_media_type.setter
    def img_media_type(self, img_media_type: str):
        self.__img_media_type = img_media_type

    @property
    def img_size(self) -> str:
        return self.__img_size

    @img_size.setter
    def img_size(self, img_size: str):
        self.__img_size = img_size

    @property
    def img_name(self) -> str:
        return self.__img_name

    @img_name.setter
    def img_name(self, img_name: str):
        self.__img_name = img_name

    @property
    def img_user(self) -> str:
        return self.__img_user

    @img_user.setter
    def img_user(self, img_user: str):
        self.__img_user = img_user

    @property
    def img_user_text(self) -> str:
        return self.__img_user_text

    @img_user_text.setter
    def img_user_text(self, img_user_text: str):
        self.__img_user_text = img_user_text

    @property
    def img_metadata(self) -> str:
        return self.__img_metadata

    @img_metadata.setter
    def img_metadata(self, img_metadata: str):
        self.__img_metadata = img_metadata

    @property
    def img_width(self) -> str:
        return self.__img_width

    @img_width.setter
    def img_width(self, img_width: str):
        self.__img_width = img_width

    @property
    def img_height(self) -> str:
        return self.__img_height

    @img_height.setter
    def img_height(self, img_height: str):
        self.__img_height = img_height

    @property
    def img_sha1(self) -> str:
        return self.__img_sha1

    @img_sha1.setter
    def img_sha1(self, img_sha1: str):
        self.__img_sha1 = img_sha1

    @property
    def img_minor_mime(self) -> str:
        return self.__img_minor_mime

    @img_minor_mime.setter
    def img_minor_mime(self, img_minor_mime: str):
        self.__img_minor_mime = img_minor_mime

class wikidb116_objectcache:

    def __init__(self, exptime: date, value: str, keyname: str):
        self.exptime = exptime
        self.value = value
        self.keyname = keyname
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def keyname(self) -> str:
        return self.__keyname

    @keyname.setter
    def keyname(self, keyname: str):
        self.__keyname = keyname

    @property
    def exptime(self) -> date:
        return self.__exptime

    @exptime.setter
    def exptime(self, exptime: date):
        self.__exptime = exptime

class wikidb116_job:

    def __init__(self, job_params: str, job_title: str, job_cmd: str, job_id: str, job_namespace: str):
        self.job_params = job_params
        self.job_title = job_title
        self.job_cmd = job_cmd
        self.job_id = job_id
        self.job_namespace = job_namespace
        
    @property
    def job_id(self) -> str:
        return self.__job_id

    @job_id.setter
    def job_id(self, job_id: str):
        self.__job_id = job_id

    @property
    def job_cmd(self) -> str:
        return self.__job_cmd

    @job_cmd.setter
    def job_cmd(self, job_cmd: str):
        self.__job_cmd = job_cmd

    @property
    def job_title(self) -> str:
        return self.__job_title

    @job_title.setter
    def job_title(self, job_title: str):
        self.__job_title = job_title

    @property
    def job_namespace(self) -> str:
        return self.__job_namespace

    @job_namespace.setter
    def job_namespace(self, job_namespace: str):
        self.__job_namespace = job_namespace

    @property
    def job_params(self) -> str:
        return self.__job_params

    @job_params.setter
    def job_params(self, job_params: str):
        self.__job_params = job_params

class wikidb116_interwiki:

    def __init__(self, iw_trans: int, iw_url: str, iw_prefix: str, iw_local: int):
        self.iw_trans = iw_trans
        self.iw_url = iw_url
        self.iw_prefix = iw_prefix
        self.iw_local = iw_local
        
    @property
    def iw_prefix(self) -> str:
        return self.__iw_prefix

    @iw_prefix.setter
    def iw_prefix(self, iw_prefix: str):
        self.__iw_prefix = iw_prefix

    @property
    def iw_local(self) -> int:
        return self.__iw_local

    @iw_local.setter
    def iw_local(self, iw_local: int):
        self.__iw_local = iw_local

    @property
    def iw_url(self) -> str:
        return self.__iw_url

    @iw_url.setter
    def iw_url(self, iw_url: str):
        self.__iw_url = iw_url

    @property
    def iw_trans(self) -> int:
        return self.__iw_trans

    @iw_trans.setter
    def iw_trans(self, iw_trans: int):
        self.__iw_trans = iw_trans

class wikidb116_watchlist:

    def __init__(self, wl_title: str, wl_namespace: str, wl_notificationtimestamp: str, wl_user: str):
        self.wl_title = wl_title
        self.wl_namespace = wl_namespace
        self.wl_notificationtimestamp = wl_notificationtimestamp
        self.wl_user = wl_user
        
    @property
    def wl_notificationtimestamp(self) -> str:
        return self.__wl_notificationtimestamp

    @wl_notificationtimestamp.setter
    def wl_notificationtimestamp(self, wl_notificationtimestamp: str):
        self.__wl_notificationtimestamp = wl_notificationtimestamp

    @property
    def wl_namespace(self) -> str:
        return self.__wl_namespace

    @wl_namespace.setter
    def wl_namespace(self, wl_namespace: str):
        self.__wl_namespace = wl_namespace

    @property
    def wl_title(self) -> str:
        return self.__wl_title

    @wl_title.setter
    def wl_title(self, wl_title: str):
        self.__wl_title = wl_title

    @property
    def wl_user(self) -> str:
        return self.__wl_user

    @wl_user.setter
    def wl_user(self, wl_user: str):
        self.__wl_user = wl_user

class wikidb116_filearchive:

    def __init__(self, fa_media_type: str, fa_storage_key: str, fa_bits: str, fa_id: str, fa_size: str, fa_user_text: str, fa_major_mime: str, fa_deleted_timestamp: str, fa_minor_mime: str, fa_storage_group: str, fa_width: str, fa_height: str, fa_deleted: int, fa_metadata: str, fa_description: str, fa_deleted_reason: str, fa_archive_name: str, fa_name: str, fa_user: str, fa_timestamp: str, fa_deleted_user: str):
        self.fa_media_type = fa_media_type
        self.fa_storage_key = fa_storage_key
        self.fa_bits = fa_bits
        self.fa_id = fa_id
        self.fa_size = fa_size
        self.fa_user_text = fa_user_text
        self.fa_major_mime = fa_major_mime
        self.fa_deleted_timestamp = fa_deleted_timestamp
        self.fa_minor_mime = fa_minor_mime
        self.fa_storage_group = fa_storage_group
        self.fa_width = fa_width
        self.fa_height = fa_height
        self.fa_deleted = fa_deleted
        self.fa_metadata = fa_metadata
        self.fa_description = fa_description
        self.fa_deleted_reason = fa_deleted_reason
        self.fa_archive_name = fa_archive_name
        self.fa_name = fa_name
        self.fa_user = fa_user
        self.fa_timestamp = fa_timestamp
        self.fa_deleted_user = fa_deleted_user
        
    @property
    def fa_storage_group(self) -> str:
        return self.__fa_storage_group

    @fa_storage_group.setter
    def fa_storage_group(self, fa_storage_group: str):
        self.__fa_storage_group = fa_storage_group

    @property
    def fa_size(self) -> str:
        return self.__fa_size

    @fa_size.setter
    def fa_size(self, fa_size: str):
        self.__fa_size = fa_size

    @property
    def fa_id(self) -> str:
        return self.__fa_id

    @fa_id.setter
    def fa_id(self, fa_id: str):
        self.__fa_id = fa_id

    @property
    def fa_archive_name(self) -> str:
        return self.__fa_archive_name

    @fa_archive_name.setter
    def fa_archive_name(self, fa_archive_name: str):
        self.__fa_archive_name = fa_archive_name

    @property
    def fa_storage_key(self) -> str:
        return self.__fa_storage_key

    @fa_storage_key.setter
    def fa_storage_key(self, fa_storage_key: str):
        self.__fa_storage_key = fa_storage_key

    @property
    def fa_metadata(self) -> str:
        return self.__fa_metadata

    @fa_metadata.setter
    def fa_metadata(self, fa_metadata: str):
        self.__fa_metadata = fa_metadata

    @property
    def fa_timestamp(self) -> str:
        return self.__fa_timestamp

    @fa_timestamp.setter
    def fa_timestamp(self, fa_timestamp: str):
        self.__fa_timestamp = fa_timestamp

    @property
    def fa_user(self) -> str:
        return self.__fa_user

    @fa_user.setter
    def fa_user(self, fa_user: str):
        self.__fa_user = fa_user

    @property
    def fa_deleted_user(self) -> str:
        return self.__fa_deleted_user

    @fa_deleted_user.setter
    def fa_deleted_user(self, fa_deleted_user: str):
        self.__fa_deleted_user = fa_deleted_user

    @property
    def fa_deleted_timestamp(self) -> str:
        return self.__fa_deleted_timestamp

    @fa_deleted_timestamp.setter
    def fa_deleted_timestamp(self, fa_deleted_timestamp: str):
        self.__fa_deleted_timestamp = fa_deleted_timestamp

    @property
    def fa_deleted_reason(self) -> str:
        return self.__fa_deleted_reason

    @fa_deleted_reason.setter
    def fa_deleted_reason(self, fa_deleted_reason: str):
        self.__fa_deleted_reason = fa_deleted_reason

    @property
    def fa_bits(self) -> str:
        return self.__fa_bits

    @fa_bits.setter
    def fa_bits(self, fa_bits: str):
        self.__fa_bits = fa_bits

    @property
    def fa_width(self) -> str:
        return self.__fa_width

    @fa_width.setter
    def fa_width(self, fa_width: str):
        self.__fa_width = fa_width

    @property
    def fa_name(self) -> str:
        return self.__fa_name

    @fa_name.setter
    def fa_name(self, fa_name: str):
        self.__fa_name = fa_name

    @property
    def fa_deleted(self) -> int:
        return self.__fa_deleted

    @fa_deleted.setter
    def fa_deleted(self, fa_deleted: int):
        self.__fa_deleted = fa_deleted

    @property
    def fa_description(self) -> str:
        return self.__fa_description

    @fa_description.setter
    def fa_description(self, fa_description: str):
        self.__fa_description = fa_description

    @property
    def fa_minor_mime(self) -> str:
        return self.__fa_minor_mime

    @fa_minor_mime.setter
    def fa_minor_mime(self, fa_minor_mime: str):
        self.__fa_minor_mime = fa_minor_mime

    @property
    def fa_user_text(self) -> str:
        return self.__fa_user_text

    @fa_user_text.setter
    def fa_user_text(self, fa_user_text: str):
        self.__fa_user_text = fa_user_text

    @property
    def fa_height(self) -> str:
        return self.__fa_height

    @fa_height.setter
    def fa_height(self, fa_height: str):
        self.__fa_height = fa_height

    @property
    def fa_major_mime(self) -> str:
        return self.__fa_major_mime

    @fa_major_mime.setter
    def fa_major_mime(self, fa_major_mime: str):
        self.__fa_major_mime = fa_major_mime

    @property
    def fa_media_type(self) -> str:
        return self.__fa_media_type

    @fa_media_type.setter
    def fa_media_type(self, fa_media_type: str):
        self.__fa_media_type = fa_media_type

class wikidb116_hitcounter:

    def __init__(self, hc_id: str):
        self.hc_id = hc_id
        
    @property
    def hc_id(self) -> str:
        return self.__hc_id

    @hc_id.setter
    def hc_id(self, hc_id: str):
        self.__hc_id = hc_id

class wikidb116_templatelinks:

    def __init__(self, tl_from: str, tl_title: str, tl_namespace: str):
        self.tl_from = tl_from
        self.tl_title = tl_title
        self.tl_namespace = tl_namespace
        
    @property
    def tl_namespace(self) -> str:
        return self.__tl_namespace

    @tl_namespace.setter
    def tl_namespace(self, tl_namespace: str):
        self.__tl_namespace = tl_namespace

    @property
    def tl_from(self) -> str:
        return self.__tl_from

    @tl_from.setter
    def tl_from(self, tl_from: str):
        self.__tl_from = tl_from

    @property
    def tl_title(self) -> str:
        return self.__tl_title

    @tl_title.setter
    def tl_title(self, tl_title: str):
        self.__tl_title = tl_title

class wikidb116_page_restrictions:

    def __init__(self, pr_user: str, pr_type: str, pr_page: str, pr_expiry: str, pr_cascade: int, pr_id: str, pr_level: str):
        self.pr_user = pr_user
        self.pr_type = pr_type
        self.pr_page = pr_page
        self.pr_expiry = pr_expiry
        self.pr_cascade = pr_cascade
        self.pr_id = pr_id
        self.pr_level = pr_level
        
    @property
    def pr_cascade(self) -> int:
        return self.__pr_cascade

    @pr_cascade.setter
    def pr_cascade(self, pr_cascade: int):
        self.__pr_cascade = pr_cascade

    @property
    def pr_id(self) -> str:
        return self.__pr_id

    @pr_id.setter
    def pr_id(self, pr_id: str):
        self.__pr_id = pr_id

    @property
    def pr_type(self) -> str:
        return self.__pr_type

    @pr_type.setter
    def pr_type(self, pr_type: str):
        self.__pr_type = pr_type

    @property
    def pr_level(self) -> str:
        return self.__pr_level

    @pr_level.setter
    def pr_level(self, pr_level: str):
        self.__pr_level = pr_level

    @property
    def pr_page(self) -> str:
        return self.__pr_page

    @pr_page.setter
    def pr_page(self, pr_page: str):
        self.__pr_page = pr_page

    @property
    def pr_expiry(self) -> str:
        return self.__pr_expiry

    @pr_expiry.setter
    def pr_expiry(self, pr_expiry: str):
        self.__pr_expiry = pr_expiry

    @property
    def pr_user(self) -> str:
        return self.__pr_user

    @pr_user.setter
    def pr_user(self, pr_user: str):
        self.__pr_user = pr_user

class wikidb116_protected_titles:

    def __init__(self, pt_namespace: str, pt_expiry: str, pt_title: str, pt_create_perm: str, pt_user: str, pt_timestamp: str, pt_reason: str):
        self.pt_namespace = pt_namespace
        self.pt_expiry = pt_expiry
        self.pt_title = pt_title
        self.pt_create_perm = pt_create_perm
        self.pt_user = pt_user
        self.pt_timestamp = pt_timestamp
        self.pt_reason = pt_reason
        
    @property
    def pt_timestamp(self) -> str:
        return self.__pt_timestamp

    @pt_timestamp.setter
    def pt_timestamp(self, pt_timestamp: str):
        self.__pt_timestamp = pt_timestamp

    @property
    def pt_namespace(self) -> str:
        return self.__pt_namespace

    @pt_namespace.setter
    def pt_namespace(self, pt_namespace: str):
        self.__pt_namespace = pt_namespace

    @property
    def pt_create_perm(self) -> str:
        return self.__pt_create_perm

    @pt_create_perm.setter
    def pt_create_perm(self, pt_create_perm: str):
        self.__pt_create_perm = pt_create_perm

    @property
    def pt_title(self) -> str:
        return self.__pt_title

    @pt_title.setter
    def pt_title(self, pt_title: str):
        self.__pt_title = pt_title

    @property
    def pt_user(self) -> str:
        return self.__pt_user

    @pt_user.setter
    def pt_user(self, pt_user: str):
        self.__pt_user = pt_user

    @property
    def pt_expiry(self) -> str:
        return self.__pt_expiry

    @pt_expiry.setter
    def pt_expiry(self, pt_expiry: str):
        self.__pt_expiry = pt_expiry

    @property
    def pt_reason(self) -> str:
        return self.__pt_reason

    @pt_reason.setter
    def pt_reason(self, pt_reason: str):
        self.__pt_reason = pt_reason

class wikidb116_querycache_info:

    def __init__(self, qci_type: str, qci_timestamp: str):
        self.qci_type = qci_type
        self.qci_timestamp = qci_timestamp
        
    @property
    def qci_type(self) -> str:
        return self.__qci_type

    @qci_type.setter
    def qci_type(self, qci_type: str):
        self.__qci_type = qci_type

    @property
    def qci_timestamp(self) -> str:
        return self.__qci_timestamp

    @qci_timestamp.setter
    def qci_timestamp(self, qci_timestamp: str):
        self.__qci_timestamp = qci_timestamp

class wikidb116_user:

    def __init__(self, user_touched: str, user_email_authenticated: str, user_newpass_time: str, user_options: str, user_password: str, user_registration: str, user_id: str, user_editcount: str, user_email: str, user_newpassword: str, user_email_token: str, user_email_token_expires: str, user_name: str, user_token: str, user_real_name: str):
        self.user_touched = user_touched
        self.user_email_authenticated = user_email_authenticated
        self.user_newpass_time = user_newpass_time
        self.user_options = user_options
        self.user_password = user_password
        self.user_registration = user_registration
        self.user_id = user_id
        self.user_editcount = user_editcount
        self.user_email = user_email
        self.user_newpassword = user_newpassword
        self.user_email_token = user_email_token
        self.user_email_token_expires = user_email_token_expires
        self.user_name = user_name
        self.user_token = user_token
        self.user_real_name = user_real_name
        
    @property
    def user_password(self) -> str:
        return self.__user_password

    @user_password.setter
    def user_password(self, user_password: str):
        self.__user_password = user_password

    @property
    def user_email_token(self) -> str:
        return self.__user_email_token

    @user_email_token.setter
    def user_email_token(self, user_email_token: str):
        self.__user_email_token = user_email_token

    @property
    def user_token(self) -> str:
        return self.__user_token

    @user_token.setter
    def user_token(self, user_token: str):
        self.__user_token = user_token

    @property
    def user_email_authenticated(self) -> str:
        return self.__user_email_authenticated

    @user_email_authenticated.setter
    def user_email_authenticated(self, user_email_authenticated: str):
        self.__user_email_authenticated = user_email_authenticated

    @property
    def user_newpass_time(self) -> str:
        return self.__user_newpass_time

    @user_newpass_time.setter
    def user_newpass_time(self, user_newpass_time: str):
        self.__user_newpass_time = user_newpass_time

    @property
    def user_real_name(self) -> str:
        return self.__user_real_name

    @user_real_name.setter
    def user_real_name(self, user_real_name: str):
        self.__user_real_name = user_real_name

    @property
    def user_id(self) -> str:
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self.__user_id = user_id

    @property
    def user_newpassword(self) -> str:
        return self.__user_newpassword

    @user_newpassword.setter
    def user_newpassword(self, user_newpassword: str):
        self.__user_newpassword = user_newpassword

    @property
    def user_editcount(self) -> str:
        return self.__user_editcount

    @user_editcount.setter
    def user_editcount(self, user_editcount: str):
        self.__user_editcount = user_editcount

    @property
    def user_name(self) -> str:
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name: str):
        self.__user_name = user_name

    @property
    def user_options(self) -> str:
        return self.__user_options

    @user_options.setter
    def user_options(self, user_options: str):
        self.__user_options = user_options

    @property
    def user_registration(self) -> str:
        return self.__user_registration

    @user_registration.setter
    def user_registration(self, user_registration: str):
        self.__user_registration = user_registration

    @property
    def user_touched(self) -> str:
        return self.__user_touched

    @user_touched.setter
    def user_touched(self, user_touched: str):
        self.__user_touched = user_touched

    @property
    def user_email(self) -> str:
        return self.__user_email

    @user_email.setter
    def user_email(self, user_email: str):
        self.__user_email = user_email

    @property
    def user_email_token_expires(self) -> str:
        return self.__user_email_token_expires

    @user_email_token_expires.setter
    def user_email_token_expires(self, user_email_token_expires: str):
        self.__user_email_token_expires = user_email_token_expires

class wikidb116_categorylinks:

    def __init__(self, cl_to: str, cl_from: str, cl_sortkey: str, cl_timestamp: date):
        self.cl_to = cl_to
        self.cl_from = cl_from
        self.cl_sortkey = cl_sortkey
        self.cl_timestamp = cl_timestamp
        
    @property
    def cl_to(self) -> str:
        return self.__cl_to

    @cl_to.setter
    def cl_to(self, cl_to: str):
        self.__cl_to = cl_to

    @property
    def cl_sortkey(self) -> str:
        return self.__cl_sortkey

    @cl_sortkey.setter
    def cl_sortkey(self, cl_sortkey: str):
        self.__cl_sortkey = cl_sortkey

    @property
    def cl_from(self) -> str:
        return self.__cl_from

    @cl_from.setter
    def cl_from(self, cl_from: str):
        self.__cl_from = cl_from

    @property
    def cl_timestamp(self) -> date:
        return self.__cl_timestamp

    @cl_timestamp.setter
    def cl_timestamp(self, cl_timestamp: date):
        self.__cl_timestamp = cl_timestamp

class wikidb116_trackbacks:

    def __init__(self, tb_name: str, tb_title: str, tb_url: str, tb_ex: str, tb_id: str, tb_page: str):
        self.tb_name = tb_name
        self.tb_title = tb_title
        self.tb_url = tb_url
        self.tb_ex = tb_ex
        self.tb_id = tb_id
        self.tb_page = tb_page
        
    @property
    def tb_name(self) -> str:
        return self.__tb_name

    @tb_name.setter
    def tb_name(self, tb_name: str):
        self.__tb_name = tb_name

    @property
    def tb_id(self) -> str:
        return self.__tb_id

    @tb_id.setter
    def tb_id(self, tb_id: str):
        self.__tb_id = tb_id

    @property
    def tb_page(self) -> str:
        return self.__tb_page

    @tb_page.setter
    def tb_page(self, tb_page: str):
        self.__tb_page = tb_page

    @property
    def tb_title(self) -> str:
        return self.__tb_title

    @tb_title.setter
    def tb_title(self, tb_title: str):
        self.__tb_title = tb_title

    @property
    def tb_ex(self) -> str:
        return self.__tb_ex

    @tb_ex.setter
    def tb_ex(self, tb_ex: str):
        self.__tb_ex = tb_ex

    @property
    def tb_url(self) -> str:
        return self.__tb_url

    @tb_url.setter
    def tb_url(self, tb_url: str):
        self.__tb_url = tb_url

class wikidb116_math:

    def __init__(self, math_outputhash: str, math_inputhash: str, math_html: str, math_mathml: str, math_html_conservativeness: int):
        self.math_outputhash = math_outputhash
        self.math_inputhash = math_inputhash
        self.math_html = math_html
        self.math_mathml = math_mathml
        self.math_html_conservativeness = math_html_conservativeness
        
    @property
    def math_html_conservativeness(self) -> int:
        return self.__math_html_conservativeness

    @math_html_conservativeness.setter
    def math_html_conservativeness(self, math_html_conservativeness: int):
        self.__math_html_conservativeness = math_html_conservativeness

    @property
    def math_mathml(self) -> str:
        return self.__math_mathml

    @math_mathml.setter
    def math_mathml(self, math_mathml: str):
        self.__math_mathml = math_mathml

    @property
    def math_outputhash(self) -> str:
        return self.__math_outputhash

    @math_outputhash.setter
    def math_outputhash(self, math_outputhash: str):
        self.__math_outputhash = math_outputhash

    @property
    def math_html(self) -> str:
        return self.__math_html

    @math_html.setter
    def math_html(self, math_html: str):
        self.__math_html = math_html

    @property
    def math_inputhash(self) -> str:
        return self.__math_inputhash

    @math_inputhash.setter
    def math_inputhash(self, math_inputhash: str):
        self.__math_inputhash = math_inputhash
