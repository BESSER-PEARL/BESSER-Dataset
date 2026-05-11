





import java.util.List;
import java.util.ArrayList;

public class wikidb119_recentchanges  {

    private String rc_cur_time;
    private int rc_new;
    private String rc_moved_to_title;
    private String rc_last_oldid;
    private String rc_new_len;
    private String rc_log_action;
    private String rc_timestamp;
    private String rc_user_text;
    private String rc_this_oldid;
    private String rc_comment;
    private String rc_namespace;
    private int rc_type;
    private String rc_ip;
    private int rc_deleted;
    private String rc_log_type;
    private String rc_logid;
    private String rc_id;
    private String rc_old_len;
    private String rc_params;
    private int rc_bot;
    private String rc_cur_id;
    private String rc_user;
    private int rc_patrolled;
    private String rc_title;
    private int rc_moved_to_ns;
    private int rc_minor;



    public wikidb119_recentchanges(
        String rc_cur_time,        int rc_new,        String rc_moved_to_title,        String rc_last_oldid,        String rc_new_len,        String rc_log_action,        String rc_timestamp,        String rc_user_text,        String rc_this_oldid,        String rc_comment,        String rc_namespace,        int rc_type,        String rc_ip,        int rc_deleted,        String rc_log_type,        String rc_logid,        String rc_id,        String rc_old_len,        String rc_params,        int rc_bot,        String rc_cur_id,        String rc_user,        int rc_patrolled,        String rc_title,        int rc_moved_to_ns,        int rc_minor    ) {
        this.rc_cur_time = rc_cur_time;
        this.rc_new = rc_new;
        this.rc_moved_to_title = rc_moved_to_title;
        this.rc_last_oldid = rc_last_oldid;
        this.rc_new_len = rc_new_len;
        this.rc_log_action = rc_log_action;
        this.rc_timestamp = rc_timestamp;
        this.rc_user_text = rc_user_text;
        this.rc_this_oldid = rc_this_oldid;
        this.rc_comment = rc_comment;
        this.rc_namespace = rc_namespace;
        this.rc_type = rc_type;
        this.rc_ip = rc_ip;
        this.rc_deleted = rc_deleted;
        this.rc_log_type = rc_log_type;
        this.rc_logid = rc_logid;
        this.rc_id = rc_id;
        this.rc_old_len = rc_old_len;
        this.rc_params = rc_params;
        this.rc_bot = rc_bot;
        this.rc_cur_id = rc_cur_id;
        this.rc_user = rc_user;
        this.rc_patrolled = rc_patrolled;
        this.rc_title = rc_title;
        this.rc_moved_to_ns = rc_moved_to_ns;
        this.rc_minor = rc_minor;
    }


    public String getRc_cur_time() {
        return rc_cur_time;
    }

    public void setRc_cur_time(String rc_cur_time) {
        this.rc_cur_time = rc_cur_time;
    }
    public int getRc_new() {
        return rc_new;
    }

    public void setRc_new(int rc_new) {
        this.rc_new = rc_new;
    }
    public String getRc_moved_to_title() {
        return rc_moved_to_title;
    }

    public void setRc_moved_to_title(String rc_moved_to_title) {
        this.rc_moved_to_title = rc_moved_to_title;
    }
    public String getRc_last_oldid() {
        return rc_last_oldid;
    }

    public void setRc_last_oldid(String rc_last_oldid) {
        this.rc_last_oldid = rc_last_oldid;
    }
    public String getRc_new_len() {
        return rc_new_len;
    }

    public void setRc_new_len(String rc_new_len) {
        this.rc_new_len = rc_new_len;
    }
    public String getRc_log_action() {
        return rc_log_action;
    }

    public void setRc_log_action(String rc_log_action) {
        this.rc_log_action = rc_log_action;
    }
    public String getRc_timestamp() {
        return rc_timestamp;
    }

    public void setRc_timestamp(String rc_timestamp) {
        this.rc_timestamp = rc_timestamp;
    }
    public String getRc_user_text() {
        return rc_user_text;
    }

    public void setRc_user_text(String rc_user_text) {
        this.rc_user_text = rc_user_text;
    }
    public String getRc_this_oldid() {
        return rc_this_oldid;
    }

    public void setRc_this_oldid(String rc_this_oldid) {
        this.rc_this_oldid = rc_this_oldid;
    }
    public String getRc_comment() {
        return rc_comment;
    }

    public void setRc_comment(String rc_comment) {
        this.rc_comment = rc_comment;
    }
    public String getRc_namespace() {
        return rc_namespace;
    }

    public void setRc_namespace(String rc_namespace) {
        this.rc_namespace = rc_namespace;
    }
    public int getRc_type() {
        return rc_type;
    }

    public void setRc_type(int rc_type) {
        this.rc_type = rc_type;
    }
    public String getRc_ip() {
        return rc_ip;
    }

    public void setRc_ip(String rc_ip) {
        this.rc_ip = rc_ip;
    }
    public int getRc_deleted() {
        return rc_deleted;
    }

    public void setRc_deleted(int rc_deleted) {
        this.rc_deleted = rc_deleted;
    }
    public String getRc_log_type() {
        return rc_log_type;
    }

    public void setRc_log_type(String rc_log_type) {
        this.rc_log_type = rc_log_type;
    }
    public String getRc_logid() {
        return rc_logid;
    }

    public void setRc_logid(String rc_logid) {
        this.rc_logid = rc_logid;
    }
    public String getRc_id() {
        return rc_id;
    }

    public void setRc_id(String rc_id) {
        this.rc_id = rc_id;
    }
    public String getRc_old_len() {
        return rc_old_len;
    }

    public void setRc_old_len(String rc_old_len) {
        this.rc_old_len = rc_old_len;
    }
    public String getRc_params() {
        return rc_params;
    }

    public void setRc_params(String rc_params) {
        this.rc_params = rc_params;
    }
    public int getRc_bot() {
        return rc_bot;
    }

    public void setRc_bot(int rc_bot) {
        this.rc_bot = rc_bot;
    }
    public String getRc_cur_id() {
        return rc_cur_id;
    }

    public void setRc_cur_id(String rc_cur_id) {
        this.rc_cur_id = rc_cur_id;
    }
    public String getRc_user() {
        return rc_user;
    }

    public void setRc_user(String rc_user) {
        this.rc_user = rc_user;
    }
    public int getRc_patrolled() {
        return rc_patrolled;
    }

    public void setRc_patrolled(int rc_patrolled) {
        this.rc_patrolled = rc_patrolled;
    }
    public String getRc_title() {
        return rc_title;
    }

    public void setRc_title(String rc_title) {
        this.rc_title = rc_title;
    }
    public int getRc_moved_to_ns() {
        return rc_moved_to_ns;
    }

    public void setRc_moved_to_ns(int rc_moved_to_ns) {
        this.rc_moved_to_ns = rc_moved_to_ns;
    }
    public int getRc_minor() {
        return rc_minor;
    }

    public void setRc_minor(int rc_minor) {
        this.rc_minor = rc_minor;
    }


}