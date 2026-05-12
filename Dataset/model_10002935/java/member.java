





import java.util.List;
import java.util.ArrayList;

public class member  {

    private String name;
    private String password;
    private String memberType;



    public member(
        String name,        String password,        String memberType    ) {
        this.name = name;
        this.password = password;
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
    public String getMembertype() {
        return memberType;
    }

    public void setMembertype(String memberType) {
        this.memberType = memberType;
    }


}