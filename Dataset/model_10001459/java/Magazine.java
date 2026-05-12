





import java.util.List;
import java.util.ArrayList;

public class Magazine  {

    private String name;
    private int issueNum;
    private String location;



    public Magazine(
        String name,        int issueNum,        String location    ) {
        this.name = name;
        this.issueNum = issueNum;
        this.location = location;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getIssuenum() {
        return issueNum;
    }

    public void setIssuenum(int issueNum) {
        this.issueNum = issueNum;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}