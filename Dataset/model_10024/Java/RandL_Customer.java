





import java.util.List;
import java.util.ArrayList;

public class RandL_Customer  {

    private String age;
    private String gender;
    private String title;
    private String name;
    private String isMale;





    private RandL_LoyaltyProgram randl_loyaltyprogram;




    private RandL_CustomerCard randl_customercard;




    private RandL_Date randl_date;




    private List<RandL_LoyaltyProgram> randl_loyaltyprograms;




    private List<RandL_CustomerCard> randl_customercards;




    private RandL_Membership randl_membership;




    private List<RandL_Membership> randl_memberships;


    public RandL_Customer(
        String age,        String gender,        String title,        String name,        String isMale    ) {
        this.age = age;
        this.gender = gender;
        this.title = title;
        this.name = name;
        this.isMale = isMale;
        this.randl_loyaltyprograms = new ArrayList<>();
        this.randl_customercards = new ArrayList<>();
        this.randl_memberships = new ArrayList<>();
    }

    public RandL_Customer(
        String age,        String gender,        String title,        String name,        String isMale        ArrayList<RandL_LoyaltyProgram> randl_loyaltyprograms,        ArrayList<RandL_CustomerCard> randl_customercards,        ArrayList<RandL_Membership> randl_memberships    ) {
        this.age = age;
        this.gender = gender;
        this.title = title;
        this.name = name;
        this.isMale = isMale;
        this.randl_loyaltyprograms = randl_loyaltyprograms;
        this.randl_customercards = randl_customercards;
        this.randl_memberships = randl_memberships;
    }

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsmale() {
        return isMale;
    }

    public void setIsmale(String isMale) {
        this.isMale = isMale;
    }

    public RandL_LoyaltyProgram getRandl_loyaltyprogram() {
        return randl_loyaltyprogram;
    }

    public void setRandl_loyaltyprogram(RandL_LoyaltyProgram randl_loyaltyprogram) {
        this.randl_loyaltyprogram = randl_loyaltyprogram;
    }
    public RandL_CustomerCard getRandl_customercard() {
        return randl_customercard;
    }

    public void setRandl_customercard(RandL_CustomerCard randl_customercard) {
        this.randl_customercard = randl_customercard;
    }
    public RandL_Date getRandl_date() {
        return randl_date;
    }

    public void setRandl_date(RandL_Date randl_date) {
        this.randl_date = randl_date;
    }
    public List<RandL_LoyaltyProgram> getRandl_loyaltyprograms() {
        return randl_loyaltyprograms;
    }

    public void addRandl_loyaltyprogram(Randl_loyaltyprogram randl_loyaltyprogram) {
        this.randl_loyaltyprograms.add(randl_loyaltyprogram);
    }
    public List<RandL_CustomerCard> getRandl_customercards() {
        return randl_customercards;
    }

    public void addRandl_customercard(Randl_customercard randl_customercard) {
        this.randl_customercards.add(randl_customercard);
    }
    public RandL_Membership getRandl_membership() {
        return randl_membership;
    }

    public void setRandl_membership(RandL_Membership randl_membership) {
        this.randl_membership = randl_membership;
    }
    public List<RandL_Membership> getRandl_memberships() {
        return randl_memberships;
    }

    public void addRandl_membership(Randl_membership randl_membership) {
        this.randl_memberships.add(randl_membership);
    }

}