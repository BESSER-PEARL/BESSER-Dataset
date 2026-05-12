





import java.util.List;
import java.util.ArrayList;

public class faculty_Actor  {






    private logout_external logout_external;




    private send_attendance_sms_external send_attendance_sms_external;




    private login_external login_external;


    public faculty_Actor(
    ) {
    }



    public logout_external getLogout_external() {
        return logout_external;
    }

    public void setLogout_external(logout_external logout_external) {
        this.logout_external = logout_external;
    }
    public send_attendance_sms_external getSend_attendance_sms_external() {
        return send_attendance_sms_external;
    }

    public void setSend_attendance_sms_external(send_attendance_sms_external send_attendance_sms_external) {
        this.send_attendance_sms_external = send_attendance_sms_external;
    }
    public login_external getLogin_external() {
        return login_external;
    }

    public void setLogin_external(login_external login_external) {
        this.login_external = login_external;
    }

}