





import java.util.List;
import java.util.ArrayList;

public class oogen_OOType  {

    private int arrayDimensions;
    private String baseType;
    private int numberOfIndirections;
    private String collectionType;





    private oogen_OOEnumeration oogen_ooenumeration;




    private List<oogen_OOExpression> oogen_ooexpressions;




    private oogen_OOClass oogen_ooclass;




    private oogen_OOMethod oogen_oomethod;




    private oogen_OOVariable oogen_oovariable;


    public oogen_OOType(
        int arrayDimensions,        String baseType,        int numberOfIndirections,        String collectionType    ) {
        this.arrayDimensions = arrayDimensions;
        this.baseType = baseType;
        this.numberOfIndirections = numberOfIndirections;
        this.collectionType = collectionType;
        this.oogen_ooexpressions = new ArrayList<>();
    }

    public oogen_OOType(
        int arrayDimensions,        String baseType,        int numberOfIndirections,        String collectionType        ArrayList<oogen_OOExpression> oogen_ooexpressions    ) {
        this.arrayDimensions = arrayDimensions;
        this.baseType = baseType;
        this.numberOfIndirections = numberOfIndirections;
        this.collectionType = collectionType;
        this.oogen_ooexpressions = oogen_ooexpressions;
    }

    public int getArraydimensions() {
        return arrayDimensions;
    }

    public void setArraydimensions(int arrayDimensions) {
        this.arrayDimensions = arrayDimensions;
    }
    public String getBasetype() {
        return baseType;
    }

    public void setBasetype(String baseType) {
        this.baseType = baseType;
    }
    public int getNumberofindirections() {
        return numberOfIndirections;
    }

    public void setNumberofindirections(int numberOfIndirections) {
        this.numberOfIndirections = numberOfIndirections;
    }
    public String getCollectiontype() {
        return collectionType;
    }

    public void setCollectiontype(String collectionType) {
        this.collectionType = collectionType;
    }

    public oogen_OOEnumeration getOogen_ooenumeration() {
        return oogen_ooenumeration;
    }

    public void setOogen_ooenumeration(oogen_OOEnumeration oogen_ooenumeration) {
        this.oogen_ooenumeration = oogen_ooenumeration;
    }
    public List<oogen_OOExpression> getOogen_ooexpressions() {
        return oogen_ooexpressions;
    }

    public void addOogen_ooexpression(Oogen_ooexpression oogen_ooexpression) {
        this.oogen_ooexpressions.add(oogen_ooexpression);
    }
    public oogen_OOClass getOogen_ooclass() {
        return oogen_ooclass;
    }

    public void setOogen_ooclass(oogen_OOClass oogen_ooclass) {
        this.oogen_ooclass = oogen_ooclass;
    }
    public oogen_OOMethod getOogen_oomethod() {
        return oogen_oomethod;
    }

    public void setOogen_oomethod(oogen_OOMethod oogen_oomethod) {
        this.oogen_oomethod = oogen_oomethod;
    }
    public oogen_OOVariable getOogen_oovariable() {
        return oogen_oovariable;
    }

    public void setOogen_oovariable(oogen_OOVariable oogen_oovariable) {
        this.oogen_oovariable = oogen_oovariable;
    }

}