





import java.util.List;
import java.util.ArrayList;

public class member  {

    private String memberType;
    private String name;
    private String password;



    public member(
        String memberType,        String name,        String password    ) {
        this.memberType = memberType;
        this.name = name;
        this.password = password;
    }


    public String getMembertype() {
        return memberType;
    }

    public void setMembertype(String memberType) {
        this.memberType = memberType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}