





import java.util.List;
import java.util.ArrayList;

public class TypeA_B  {

    private String name;
    private String description3;
    private String description2;
    private String description1;





    private TypeA_A typea_a;


    public TypeA_B(
        String name,        String description3,        String description2,        String description1    ) {
        this.name = name;
        this.description3 = description3;
        this.description2 = description2;
        this.description1 = description1;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription3() {
        return description3;
    }

    public void setDescription3(String description3) {
        this.description3 = description3;
    }
    public String getDescription2() {
        return description2;
    }

    public void setDescription2(String description2) {
        this.description2 = description2;
    }
    public String getDescription1() {
        return description1;
    }

    public void setDescription1(String description1) {
        this.description1 = description1;
    }

    public TypeA_A getTypea_a() {
        return typea_a;
    }

    public void setTypea_a(TypeA_A typea_a) {
        this.typea_a = typea_a;
    }

}