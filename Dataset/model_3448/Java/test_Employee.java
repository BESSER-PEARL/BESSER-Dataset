





import java.util.List;
import java.util.ArrayList;

public class test_Employee extends Person {

    private String incomeLevel;



    public test_Employee(
        String incomeLevel    ) {
        super(
        );
        this.incomeLevel = incomeLevel;
    }


    public String getIncomelevel() {
        return incomeLevel;
    }

    public void setIncomelevel(String incomeLevel) {
        this.incomeLevel = incomeLevel;
    }


}