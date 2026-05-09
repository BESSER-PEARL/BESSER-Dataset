





import java.util.List;
import java.util.ArrayList;

public class familyTree_Person  {

    private String lastName;
    private String name;





    private familyTree_Male familytree_male;




    private familyTree_FamilyTree familytree_familytree;




    private familyTree_Female familytree_female;




    private familyTree_Male familytree_male;




    private familyTree_Female familytree_female;




    private familyTree_FamilyTree familytree_familytree;


    public familyTree_Person(
        String lastName,        String name    ) {
        this.lastName = lastName;
        this.name = name;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public familyTree_Male getFamilytree_male() {
        return familytree_male;
    }

    public void setFamilytree_male(familyTree_Male familytree_male) {
        this.familytree_male = familytree_male;
    }
    public familyTree_FamilyTree getFamilytree_familytree() {
        return familytree_familytree;
    }

    public void setFamilytree_familytree(familyTree_FamilyTree familytree_familytree) {
        this.familytree_familytree = familytree_familytree;
    }
    public familyTree_Female getFamilytree_female() {
        return familytree_female;
    }

    public void setFamilytree_female(familyTree_Female familytree_female) {
        this.familytree_female = familytree_female;
    }
    public familyTree_Male getFamilytree_male() {
        return familytree_male;
    }

    public void setFamilytree_male(familyTree_Male familytree_male) {
        this.familytree_male = familytree_male;
    }
    public familyTree_Female getFamilytree_female() {
        return familytree_female;
    }

    public void setFamilytree_female(familyTree_Female familytree_female) {
        this.familytree_female = familytree_female;
    }
    public familyTree_FamilyTree getFamilytree_familytree() {
        return familytree_familytree;
    }

    public void setFamilytree_familytree(familyTree_FamilyTree familytree_familytree) {
        this.familytree_familytree = familytree_familytree;
    }

}