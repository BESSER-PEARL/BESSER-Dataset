





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_Expression extends ValueSpecification {

    private String symbol;





    private ClassesProv_ValueSpecification classesprov_valuespecification;


    public ClassesProv_Expression(
        String symbol    ) {
        super(
        );
        this.symbol = symbol;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public ClassesProv_ValueSpecification getClassesprov_valuespecification() {
        return classesprov_valuespecification;
    }

    public void setClassesprov_valuespecification(ClassesProv_ValueSpecification classesprov_valuespecification) {
        this.classesprov_valuespecification = classesprov_valuespecification;
    }

}