





import java.util.List;
import java.util.ArrayList;

public class conference_Person  {

    private boolean isRegistered;
    private String gender;
    private boolean eclipseCommiter;
    private String lastname;
    private String firstname;
    private int age;





    private conference_Talk conference_talk;




    private conference_Talk conference_talk;




    private conference_Conference conference_conference;




    private List<conference_Talk> conference_talks;


    public conference_Person(
        boolean isRegistered,        String gender,        boolean eclipseCommiter,        String lastname,        String firstname,        int age    ) {
        this.isRegistered = isRegistered;
        this.gender = gender;
        this.eclipseCommiter = eclipseCommiter;
        this.lastname = lastname;
        this.firstname = firstname;
        this.age = age;
        this.conference_talks = new ArrayList<>();
    }

    public conference_Person(
        boolean isRegistered,        String gender,        boolean eclipseCommiter,        String lastname,        String firstname,        int age        ArrayList<conference_Talk> conference_talks    ) {
        this.isRegistered = isRegistered;
        this.gender = gender;
        this.eclipseCommiter = eclipseCommiter;
        this.lastname = lastname;
        this.firstname = firstname;
        this.age = age;
        this.conference_talks = conference_talks;
    }

    public boolean getIsregistered() {
        return isRegistered;
    }

    public void setIsregistered(boolean isRegistered) {
        this.isRegistered = isRegistered;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public boolean getEclipsecommiter() {
        return eclipseCommiter;
    }

    public void setEclipsecommiter(boolean eclipseCommiter) {
        this.eclipseCommiter = eclipseCommiter;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public conference_Talk getConference_talk() {
        return conference_talk;
    }

    public void setConference_talk(conference_Talk conference_talk) {
        this.conference_talk = conference_talk;
    }
    public conference_Talk getConference_talk() {
        return conference_talk;
    }

    public void setConference_talk(conference_Talk conference_talk) {
        this.conference_talk = conference_talk;
    }
    public conference_Conference getConference_conference() {
        return conference_conference;
    }

    public void setConference_conference(conference_Conference conference_conference) {
        this.conference_conference = conference_conference;
    }
    public List<conference_Talk> getConference_talks() {
        return conference_talks;
    }

    public void addConference_talk(Conference_talk conference_talk) {
        this.conference_talks.add(conference_talk);
    }

}