





import java.util.List;
import java.util.ArrayList;

public class jPQL_Float  {

    private int integerValue;
    private int fractionValue;





    private jPQL_FloatLiteral jpql_floatliteral;


    public jPQL_Float(
        int integerValue,        int fractionValue    ) {
        this.integerValue = integerValue;
        this.fractionValue = fractionValue;
    }


    public int getIntegervalue() {
        return integerValue;
    }

    public void setIntegervalue(int integerValue) {
        this.integerValue = integerValue;
    }
    public int getFractionvalue() {
        return fractionValue;
    }

    public void setFractionvalue(int fractionValue) {
        this.fractionValue = fractionValue;
    }

    public jPQL_FloatLiteral getJpql_floatliteral() {
        return jpql_floatliteral;
    }

    public void setJpql_floatliteral(jPQL_FloatLiteral jpql_floatliteral) {
        this.jpql_floatliteral = jpql_floatliteral;
    }

}