





import java.util.List;
import java.util.ArrayList;

public class Admin_  {

    private String Password;
    private String ArrayList_member_;
    private String ArrayList_worker_;





    private member member;




    private Workers workers;


    public Admin_(
        String Password,        String ArrayList_member_,        String ArrayList_worker_    ) {
        this.Password = Password;
        this.ArrayList_member_ = ArrayList_member_;
        this.ArrayList_worker_ = ArrayList_worker_;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getArraylist_member_() {
        return ArrayList_member_;
    }

    public void setArraylist_member_(String ArrayList_member_) {
        this.ArrayList_member_ = ArrayList_member_;
    }
    public String getArraylist_worker_() {
        return ArrayList_worker_;
    }

    public void setArraylist_worker_(String ArrayList_worker_) {
        this.ArrayList_worker_ = ArrayList_worker_;
    }

    public member getMember() {
        return member;
    }

    public void setMember(member member) {
        this.member = member;
    }
    public Workers getWorkers() {
        return workers;
    }

    public void setWorkers(Workers workers) {
        this.workers = workers;
    }

}