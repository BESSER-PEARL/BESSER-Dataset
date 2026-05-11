





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_Member  {

    private String visible;
    private String extraField1;
    private String extraField2;
    private String lastName;
    private String division;
    private String firstName;
    private String languages;
    private String archived;
    private String interests;
    private String birthDate;
    private String locatable;
    private String joinDate;
    private String employer;
    private String middleInitial;
    private String statusProfile;
    private String activityGroups;
    private String id;
    private String occupation;
    private String subDivision;





    private StreetAddress streetaddress;




    private PhoneNumber phonenumber;




    private PhoneNumber phonenumber;




    private PhoneNumber phonenumber;




    private List<Note> notes;




    private Organization organization;




    private PhoneNumber phonenumber;




    private FamilyMember familymember;




    private StudyDeptInfo studydeptinfo;




    private EmailAddress emailaddress;




    private LeadershipInfo leadershipinfo;


    public org_sgiusa_model_Member(
        String visible,        String extraField1,        String extraField2,        String lastName,        String division,        String firstName,        String languages,        String archived,        String interests,        String birthDate,        String locatable,        String joinDate,        String employer,        String middleInitial,        String statusProfile,        String activityGroups,        String id,        String occupation,        String subDivision    ) {
        this.visible = visible;
        this.extraField1 = extraField1;
        this.extraField2 = extraField2;
        this.lastName = lastName;
        this.division = division;
        this.firstName = firstName;
        this.languages = languages;
        this.archived = archived;
        this.interests = interests;
        this.birthDate = birthDate;
        this.locatable = locatable;
        this.joinDate = joinDate;
        this.employer = employer;
        this.middleInitial = middleInitial;
        this.statusProfile = statusProfile;
        this.activityGroups = activityGroups;
        this.id = id;
        this.occupation = occupation;
        this.subDivision = subDivision;
        this.notes = new ArrayList<>();
    }

    public org_sgiusa_model_Member(
        String visible,        String extraField1,        String extraField2,        String lastName,        String division,        String firstName,        String languages,        String archived,        String interests,        String birthDate,        String locatable,        String joinDate,        String employer,        String middleInitial,        String statusProfile,        String activityGroups,        String id,        String occupation,        String subDivision        ArrayList<Note> notes    ) {
        this.visible = visible;
        this.extraField1 = extraField1;
        this.extraField2 = extraField2;
        this.lastName = lastName;
        this.division = division;
        this.firstName = firstName;
        this.languages = languages;
        this.archived = archived;
        this.interests = interests;
        this.birthDate = birthDate;
        this.locatable = locatable;
        this.joinDate = joinDate;
        this.employer = employer;
        this.middleInitial = middleInitial;
        this.statusProfile = statusProfile;
        this.activityGroups = activityGroups;
        this.id = id;
        this.occupation = occupation;
        this.subDivision = subDivision;
        this.notes = notes;
    }

    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getExtrafield1() {
        return extraField1;
    }

    public void setExtrafield1(String extraField1) {
        this.extraField1 = extraField1;
    }
    public String getExtrafield2() {
        return extraField2;
    }

    public void setExtrafield2(String extraField2) {
        this.extraField2 = extraField2;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getDivision() {
        return division;
    }

    public void setDivision(String division) {
        this.division = division;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLanguages() {
        return languages;
    }

    public void setLanguages(String languages) {
        this.languages = languages;
    }
    public String getArchived() {
        return archived;
    }

    public void setArchived(String archived) {
        this.archived = archived;
    }
    public String getInterests() {
        return interests;
    }

    public void setInterests(String interests) {
        this.interests = interests;
    }
    public String getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(String birthDate) {
        this.birthDate = birthDate;
    }
    public String getLocatable() {
        return locatable;
    }

    public void setLocatable(String locatable) {
        this.locatable = locatable;
    }
    public String getJoindate() {
        return joinDate;
    }

    public void setJoindate(String joinDate) {
        this.joinDate = joinDate;
    }
    public String getEmployer() {
        return employer;
    }

    public void setEmployer(String employer) {
        this.employer = employer;
    }
    public String getMiddleinitial() {
        return middleInitial;
    }

    public void setMiddleinitial(String middleInitial) {
        this.middleInitial = middleInitial;
    }
    public String getStatusprofile() {
        return statusProfile;
    }

    public void setStatusprofile(String statusProfile) {
        this.statusProfile = statusProfile;
    }
    public String getActivitygroups() {
        return activityGroups;
    }

    public void setActivitygroups(String activityGroups) {
        this.activityGroups = activityGroups;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getOccupation() {
        return occupation;
    }

    public void setOccupation(String occupation) {
        this.occupation = occupation;
    }
    public String getSubdivision() {
        return subDivision;
    }

    public void setSubdivision(String subDivision) {
        this.subDivision = subDivision;
    }

    public StreetAddress getStreetaddress() {
        return streetaddress;
    }

    public void setStreetaddress(StreetAddress streetaddress) {
        this.streetaddress = streetaddress;
    }
    public PhoneNumber getPhonenumber() {
        return phonenumber;
    }

    public void setPhonenumber(PhoneNumber phonenumber) {
        this.phonenumber = phonenumber;
    }
    public PhoneNumber getPhonenumber() {
        return phonenumber;
    }

    public void setPhonenumber(PhoneNumber phonenumber) {
        this.phonenumber = phonenumber;
    }
    public PhoneNumber getPhonenumber() {
        return phonenumber;
    }

    public void setPhonenumber(PhoneNumber phonenumber) {
        this.phonenumber = phonenumber;
    }
    public List<Note> getNotes() {
        return notes;
    }

    public void addNote(Note note) {
        this.notes.add(note);
    }
    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
    }
    public PhoneNumber getPhonenumber() {
        return phonenumber;
    }

    public void setPhonenumber(PhoneNumber phonenumber) {
        this.phonenumber = phonenumber;
    }
    public FamilyMember getFamilymember() {
        return familymember;
    }

    public void setFamilymember(FamilyMember familymember) {
        this.familymember = familymember;
    }
    public StudyDeptInfo getStudydeptinfo() {
        return studydeptinfo;
    }

    public void setStudydeptinfo(StudyDeptInfo studydeptinfo) {
        this.studydeptinfo = studydeptinfo;
    }
    public EmailAddress getEmailaddress() {
        return emailaddress;
    }

    public void setEmailaddress(EmailAddress emailaddress) {
        this.emailaddress = emailaddress;
    }
    public LeadershipInfo getLeadershipinfo() {
        return leadershipinfo;
    }

    public void setLeadershipinfo(LeadershipInfo leadershipinfo) {
        this.leadershipinfo = leadershipinfo;
    }

}