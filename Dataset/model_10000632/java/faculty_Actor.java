





import java.util.List;
import java.util.ArrayList;

public class faculty_Actor  {






    private send_attendance_sms_external send_attendance_sms_external;




    private post_attendance_external post_attendance_external;




    private view_cumiliative_attendance_external view_cumiliative_attendance_external;




    private login_external login_external;




    private logout_external logout_external;


    public faculty_Actor(
    ) {
    }



    public send_attendance_sms_external getSend_attendance_sms_external() {
        return send_attendance_sms_external;
    }

    public void setSend_attendance_sms_external(send_attendance_sms_external send_attendance_sms_external) {
        this.send_attendance_sms_external = send_attendance_sms_external;
    }
    public post_attendance_external getPost_attendance_external() {
        return post_attendance_external;
    }

    public void setPost_attendance_external(post_attendance_external post_attendance_external) {
        this.post_attendance_external = post_attendance_external;
    }
    public view_cumiliative_attendance_external getView_cumiliative_attendance_external() {
        return view_cumiliative_attendance_external;
    }

    public void setView_cumiliative_attendance_external(view_cumiliative_attendance_external view_cumiliative_attendance_external) {
        this.view_cumiliative_attendance_external = view_cumiliative_attendance_external;
    }
    public login_external getLogin_external() {
        return login_external;
    }

    public void setLogin_external(login_external login_external) {
        this.login_external = login_external;
    }
    public logout_external getLogout_external() {
        return logout_external;
    }

    public void setLogout_external(logout_external logout_external) {
        this.logout_external = logout_external;
    }

}