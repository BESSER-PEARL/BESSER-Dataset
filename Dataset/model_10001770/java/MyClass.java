





import java.util.List;
import java.util.ArrayList;

public class MyClass  {

    private String attribute3;
    private String TenCoSo;
    private String attribute;
    private String attribute2;



    public MyClass(
        String attribute3,        String TenCoSo,        String attribute,        String attribute2    ) {
        this.attribute3 = attribute3;
        this.TenCoSo = TenCoSo;
        this.attribute = attribute;
        this.attribute2 = attribute2;
    }


    public String getAttribute3() {
        return attribute3;
    }

    public void setAttribute3(String attribute3) {
        this.attribute3 = attribute3;
    }
    public String getTencoso() {
        return TenCoSo;
    }

    public void setTencoso(String TenCoSo) {
        this.TenCoSo = TenCoSo;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }


}