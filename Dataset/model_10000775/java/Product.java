





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String description;
    private String attribute2;
    private String attribute5;
    private String attribute7;
    private String attribute8;
    private String name;
    private String attribute;
    private String attribute6;
    private String attribute4;
    private String attribute3;





    private List<LineItem> lineitems;


    public Product(
        String description,        String attribute2,        String attribute5,        String attribute7,        String attribute8,        String name,        String attribute,        String attribute6,        String attribute4,        String attribute3    ) {
        this.description = description;
        this.attribute2 = attribute2;
        this.attribute5 = attribute5;
        this.attribute7 = attribute7;
        this.attribute8 = attribute8;
        this.name = name;
        this.attribute = attribute;
        this.attribute6 = attribute6;
        this.attribute4 = attribute4;
        this.attribute3 = attribute3;
        this.lineitems = new ArrayList<>();
    }

    public Product(
        String description,        String attribute2,        String attribute5,        String attribute7,        String attribute8,        String name,        String attribute,        String attribute6,        String attribute4,        String attribute3        ArrayList<LineItem> lineitems    ) {
        this.description = description;
        this.attribute2 = attribute2;
        this.attribute5 = attribute5;
        this.attribute7 = attribute7;
        this.attribute8 = attribute8;
        this.name = name;
        this.attribute = attribute;
        this.attribute6 = attribute6;
        this.attribute4 = attribute4;
        this.attribute3 = attribute3;
        this.lineitems = lineitems;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public String getAttribute5() {
        return attribute5;
    }

    public void setAttribute5(String attribute5) {
        this.attribute5 = attribute5;
    }
    public String getAttribute7() {
        return attribute7;
    }

    public void setAttribute7(String attribute7) {
        this.attribute7 = attribute7;
    }
    public String getAttribute8() {
        return attribute8;
    }

    public void setAttribute8(String attribute8) {
        this.attribute8 = attribute8;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getAttribute6() {
        return attribute6;
    }

    public void setAttribute6(String attribute6) {
        this.attribute6 = attribute6;
    }
    public String getAttribute4() {
        return attribute4;
    }

    public void setAttribute4(String attribute4) {
        this.attribute4 = attribute4;
    }
    public String getAttribute3() {
        return attribute3;
    }

    public void setAttribute3(String attribute3) {
        this.attribute3 = attribute3;
    }

    public List<LineItem> getLineitems() {
        return lineitems;
    }

    public void addLineitem(Lineitem lineitem) {
        this.lineitems.add(lineitem);
    }

}