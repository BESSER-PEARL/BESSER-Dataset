





import java.util.List;
import java.util.ArrayList;

public class person  {

    private String birthday;
    private boolean gender;
    private None belongsTo;
    private String portrait;
    private String personID;
    private String name;



    public person(
        String birthday,        boolean gender,        None belongsTo,        String portrait,        String personID,        String name    ) {
        this.birthday = birthday;
        this.gender = gender;
        this.belongsTo = belongsTo;
        this.portrait = portrait;
        this.personID = personID;
        this.name = name;
    }


    public String getBirthday() {
        return birthday;
    }

    public void setBirthday(String birthday) {
        this.birthday = birthday;
    }
    public boolean getGender() {
        return gender;
    }

    public void setGender(boolean gender) {
        this.gender = gender;
    }
    public None getBelongsto() {
        return belongsTo;
    }

    public void setBelongsto(None belongsTo) {
        this.belongsTo = belongsTo;
    }
    public String getPortrait() {
        return portrait;
    }

    public void setPortrait(String portrait) {
        this.portrait = portrait;
    }
    public String getPersonid() {
        return personID;
    }

    public void setPersonid(String personID) {
        this.personID = personID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}