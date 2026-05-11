





import java.util.List;
import java.util.ArrayList;

public class RoyalAndLoyal_Customer  {

    private int age;
    private boolean isMale;
    private String name;
    private String title;
    private String gender;





    private List<RoyalAndLoyal_CustomerCard> royalandloyal_customercards;




    private RoyalAndLoyal_CustomerCard royalandloyal_customercard;




    private List<RoyalAndLoyal_Membership> royalandloyal_memberships;




    private RoyalAndLoyal_LoyaltyProgram royalandloyal_loyaltyprogram;




    private RoyalAndLoyal_Membership royalandloyal_membership;




    private RoyalAndLoyal_Date royalandloyal_date;




    private List<RoyalAndLoyal_LoyaltyProgram> royalandloyal_loyaltyprograms;


    public RoyalAndLoyal_Customer(
        int age,        boolean isMale,        String name,        String title,        String gender    ) {
        this.age = age;
        this.isMale = isMale;
        this.name = name;
        this.title = title;
        this.gender = gender;
        this.royalandloyal_customercards = new ArrayList<>();
        this.royalandloyal_memberships = new ArrayList<>();
        this.royalandloyal_loyaltyprograms = new ArrayList<>();
    }

    public RoyalAndLoyal_Customer(
        int age,        boolean isMale,        String name,        String title,        String gender        ArrayList<RoyalAndLoyal_CustomerCard> royalandloyal_customercards,        ArrayList<RoyalAndLoyal_Membership> royalandloyal_memberships,        ArrayList<RoyalAndLoyal_LoyaltyProgram> royalandloyal_loyaltyprograms    ) {
        this.age = age;
        this.isMale = isMale;
        this.name = name;
        this.title = title;
        this.gender = gender;
        this.royalandloyal_customercards = royalandloyal_customercards;
        this.royalandloyal_memberships = royalandloyal_memberships;
        this.royalandloyal_loyaltyprograms = royalandloyal_loyaltyprograms;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public boolean getIsmale() {
        return isMale;
    }

    public void setIsmale(boolean isMale) {
        this.isMale = isMale;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public List<RoyalAndLoyal_CustomerCard> getRoyalandloyal_customercards() {
        return royalandloyal_customercards;
    }

    public void addRoyalandloyal_customercard(Royalandloyal_customercard royalandloyal_customercard) {
        this.royalandloyal_customercards.add(royalandloyal_customercard);
    }
    public RoyalAndLoyal_CustomerCard getRoyalandloyal_customercard() {
        return royalandloyal_customercard;
    }

    public void setRoyalandloyal_customercard(RoyalAndLoyal_CustomerCard royalandloyal_customercard) {
        this.royalandloyal_customercard = royalandloyal_customercard;
    }
    public List<RoyalAndLoyal_Membership> getRoyalandloyal_memberships() {
        return royalandloyal_memberships;
    }

    public void addRoyalandloyal_membership(Royalandloyal_membership royalandloyal_membership) {
        this.royalandloyal_memberships.add(royalandloyal_membership);
    }
    public RoyalAndLoyal_LoyaltyProgram getRoyalandloyal_loyaltyprogram() {
        return royalandloyal_loyaltyprogram;
    }

    public void setRoyalandloyal_loyaltyprogram(RoyalAndLoyal_LoyaltyProgram royalandloyal_loyaltyprogram) {
        this.royalandloyal_loyaltyprogram = royalandloyal_loyaltyprogram;
    }
    public RoyalAndLoyal_Membership getRoyalandloyal_membership() {
        return royalandloyal_membership;
    }

    public void setRoyalandloyal_membership(RoyalAndLoyal_Membership royalandloyal_membership) {
        this.royalandloyal_membership = royalandloyal_membership;
    }
    public RoyalAndLoyal_Date getRoyalandloyal_date() {
        return royalandloyal_date;
    }

    public void setRoyalandloyal_date(RoyalAndLoyal_Date royalandloyal_date) {
        this.royalandloyal_date = royalandloyal_date;
    }
    public List<RoyalAndLoyal_LoyaltyProgram> getRoyalandloyal_loyaltyprograms() {
        return royalandloyal_loyaltyprograms;
    }

    public void addRoyalandloyal_loyaltyprogram(Royalandloyal_loyaltyprogram royalandloyal_loyaltyprogram) {
        this.royalandloyal_loyaltyprograms.add(royalandloyal_loyaltyprogram);
    }

}