





import java.util.List;
import java.util.ArrayList;

public class simpleanySimplified_Description extends MixedBaseClass {

    private String keywords;





    private List<simpleanySimplified_Description> simpleanysimplified_descriptions;




    private simpleanySimplified_Book simpleanysimplified_book;


    public simpleanySimplified_Description(
        String keywords    ) {
        super(
        );
        this.keywords = keywords;
        this.simpleanysimplified_descriptions = new ArrayList<>();
    }

    public simpleanySimplified_Description(
        String keywords        ArrayList<simpleanySimplified_Description> simpleanysimplified_descriptions    ) {
        this.keywords = keywords;
        this.simpleanysimplified_descriptions = simpleanysimplified_descriptions;
    }

    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }

    public List<simpleanySimplified_Description> getSimpleanysimplified_descriptions() {
        return simpleanysimplified_descriptions;
    }

    public void addSimpleanysimplified_description(Simpleanysimplified_description simpleanysimplified_description) {
        this.simpleanysimplified_descriptions.add(simpleanysimplified_description);
    }
    public simpleanySimplified_Book getSimpleanysimplified_book() {
        return simpleanysimplified_book;
    }

    public void setSimpleanysimplified_book(simpleanySimplified_Book simpleanysimplified_book) {
        this.simpleanysimplified_book = simpleanysimplified_book;
    }

}