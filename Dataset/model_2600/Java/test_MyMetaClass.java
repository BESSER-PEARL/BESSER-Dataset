





import java.util.List;
import java.util.ArrayList;

public class test_MyMetaClass  {

    private String enumAttr;
    private String name;





    private List<test_MyMetaClass> test_mymetaclasss;


    public test_MyMetaClass(
        String enumAttr,        String name    ) {
        this.enumAttr = enumAttr;
        this.name = name;
        this.test_mymetaclasss = new ArrayList<>();
    }

    public test_MyMetaClass(
        String enumAttr,        String name        ArrayList<test_MyMetaClass> test_mymetaclasss    ) {
        this.enumAttr = enumAttr;
        this.name = name;
        this.test_mymetaclasss = test_mymetaclasss;
    }

    public String getEnumattr() {
        return enumAttr;
    }

    public void setEnumattr(String enumAttr) {
        this.enumAttr = enumAttr;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<test_MyMetaClass> getTest_mymetaclasss() {
        return test_mymetaclasss;
    }

    public void addTest_mymetaclass(Test_mymetaclass test_mymetaclass) {
        this.test_mymetaclasss.add(test_mymetaclass);
    }

}