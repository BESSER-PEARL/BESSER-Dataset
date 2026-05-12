





import java.util.List;
import java.util.ArrayList;

public class Marriage_Demand  {

    private String Educational_status;
    private String Salary;
    private String Relation_with_proposal;
    private String Legitimate_vision;
    private String Nationality_of_the_mother;
    private String Tribe;
    private String Other_district;
    private String Nationality;
    private String Marital_status_of_the_proposer;
    private String Accept_multi_marriage;



    public Marriage_Demand(
        String Educational_status,        String Salary,        String Relation_with_proposal,        String Legitimate_vision,        String Nationality_of_the_mother,        String Tribe,        String Other_district,        String Nationality,        String Marital_status_of_the_proposer,        String Accept_multi_marriage    ) {
        this.Educational_status = Educational_status;
        this.Salary = Salary;
        this.Relation_with_proposal = Relation_with_proposal;
        this.Legitimate_vision = Legitimate_vision;
        this.Nationality_of_the_mother = Nationality_of_the_mother;
        this.Tribe = Tribe;
        this.Other_district = Other_district;
        this.Nationality = Nationality;
        this.Marital_status_of_the_proposer = Marital_status_of_the_proposer;
        this.Accept_multi_marriage = Accept_multi_marriage;
    }


    public String getEducational_status() {
        return Educational_status;
    }

    public void setEducational_status(String Educational_status) {
        this.Educational_status = Educational_status;
    }
    public String getSalary() {
        return Salary;
    }

    public void setSalary(String Salary) {
        this.Salary = Salary;
    }
    public String getRelation_with_proposal() {
        return Relation_with_proposal;
    }

    public void setRelation_with_proposal(String Relation_with_proposal) {
        this.Relation_with_proposal = Relation_with_proposal;
    }
    public String getLegitimate_vision() {
        return Legitimate_vision;
    }

    public void setLegitimate_vision(String Legitimate_vision) {
        this.Legitimate_vision = Legitimate_vision;
    }
    public String getNationality_of_the_mother() {
        return Nationality_of_the_mother;
    }

    public void setNationality_of_the_mother(String Nationality_of_the_mother) {
        this.Nationality_of_the_mother = Nationality_of_the_mother;
    }
    public String getTribe() {
        return Tribe;
    }

    public void setTribe(String Tribe) {
        this.Tribe = Tribe;
    }
    public String getOther_district() {
        return Other_district;
    }

    public void setOther_district(String Other_district) {
        this.Other_district = Other_district;
    }
    public String getNationality() {
        return Nationality;
    }

    public void setNationality(String Nationality) {
        this.Nationality = Nationality;
    }
    public String getMarital_status_of_the_proposer() {
        return Marital_status_of_the_proposer;
    }

    public void setMarital_status_of_the_proposer(String Marital_status_of_the_proposer) {
        this.Marital_status_of_the_proposer = Marital_status_of_the_proposer;
    }
    public String getAccept_multi_marriage() {
        return Accept_multi_marriage;
    }

    public void setAccept_multi_marriage(String Accept_multi_marriage) {
        this.Accept_multi_marriage = Accept_multi_marriage;
    }


}