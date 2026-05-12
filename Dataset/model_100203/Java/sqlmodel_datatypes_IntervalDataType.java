





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_IntervalDataType extends PredefinedDataType {

    private String trailingQualifier;
    private int leadingFieldPrecision;
    private int fractionalSecondsPrecision;
    private String leadingQualifier;
    private int trailingFieldPrecision;



    public sqlmodel_datatypes_IntervalDataType(
        String trailingQualifier,        int leadingFieldPrecision,        int fractionalSecondsPrecision,        String leadingQualifier,        int trailingFieldPrecision    ) {
        super(
        );
        this.trailingQualifier = trailingQualifier;
        this.leadingFieldPrecision = leadingFieldPrecision;
        this.fractionalSecondsPrecision = fractionalSecondsPrecision;
        this.leadingQualifier = leadingQualifier;
        this.trailingFieldPrecision = trailingFieldPrecision;
    }


    public String getTrailingqualifier() {
        return trailingQualifier;
    }

    public void setTrailingqualifier(String trailingQualifier) {
        this.trailingQualifier = trailingQualifier;
    }
    public int getLeadingfieldprecision() {
        return leadingFieldPrecision;
    }

    public void setLeadingfieldprecision(int leadingFieldPrecision) {
        this.leadingFieldPrecision = leadingFieldPrecision;
    }
    public int getFractionalsecondsprecision() {
        return fractionalSecondsPrecision;
    }

    public void setFractionalsecondsprecision(int fractionalSecondsPrecision) {
        this.fractionalSecondsPrecision = fractionalSecondsPrecision;
    }
    public String getLeadingqualifier() {
        return leadingQualifier;
    }

    public void setLeadingqualifier(String leadingQualifier) {
        this.leadingQualifier = leadingQualifier;
    }
    public int getTrailingfieldprecision() {
        return trailingFieldPrecision;
    }

    public void setTrailingfieldprecision(int trailingFieldPrecision) {
        this.trailingFieldPrecision = trailingFieldPrecision;
    }


}