





import java.util.List;
import java.util.ArrayList;

public class hutnArticleFamilies_Person  {

    private String name;





    private hutnArticleFamilies_Family hutnarticlefamilies_family;


    public hutnArticleFamilies_Person(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public hutnArticleFamilies_Family getHutnarticlefamilies_family() {
        return hutnarticlefamilies_family;
    }

    public void setHutnarticlefamilies_family(hutnArticleFamilies_Family hutnarticlefamilies_family) {
        this.hutnarticlefamilies_family = hutnarticlefamilies_family;
    }

}