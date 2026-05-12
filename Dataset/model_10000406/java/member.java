





import java.util.List;
import java.util.ArrayList;

public class member  {

    private String name;
    private String memberType;
    private String password;



    public member(
        String name,        String memberType,        String password    ) {
        this.name = name;
        this.memberType = memberType;
        this.password = password;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMembertype() {
        return memberType;
    }

    public void setMembertype(String memberType) {
        this.memberType = memberType;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}