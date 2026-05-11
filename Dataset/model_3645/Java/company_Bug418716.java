





import java.util.List;
import java.util.ArrayList;

public class company_Bug418716  {

    private int AttributeWithoutInitital;
    private int AttributeWithInitital;



    public company_Bug418716(
        int AttributeWithoutInitital,        int AttributeWithInitital    ) {
        this.AttributeWithoutInitital = AttributeWithoutInitital;
        this.AttributeWithInitital = AttributeWithInitital;
    }


    public int getAttributewithoutinitital() {
        return AttributeWithoutInitital;
    }

    public void setAttributewithoutinitital(int AttributeWithoutInitital) {
        this.AttributeWithoutInitital = AttributeWithoutInitital;
    }
    public int getAttributewithinitital() {
        return AttributeWithInitital;
    }

    public void setAttributewithinitital(int AttributeWithInitital) {
        this.AttributeWithInitital = AttributeWithInitital;
    }


}