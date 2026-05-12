





import java.util.List;
import java.util.ArrayList;

public class research_team_Person  {

    private String affiliation;
    private String name;
    private String firstname;
    private String mail;
    private String phone;





    private research_team_Team research_team_team;




    private research_team_Team research_team_team;


    public research_team_Person(
        String affiliation,        String name,        String firstname,        String mail,        String phone    ) {
        this.affiliation = affiliation;
        this.name = name;
        this.firstname = firstname;
        this.mail = mail;
        this.phone = phone;
    }


    public String getAffiliation() {
        return affiliation;
    }

    public void setAffiliation(String affiliation) {
        this.affiliation = affiliation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public research_team_Team getResearch_team_team() {
        return research_team_team;
    }

    public void setResearch_team_team(research_team_Team research_team_team) {
        this.research_team_team = research_team_team;
    }
    public research_team_Team getResearch_team_team() {
        return research_team_team;
    }

    public void setResearch_team_team(research_team_Team research_team_team) {
        this.research_team_team = research_team_team;
    }

}