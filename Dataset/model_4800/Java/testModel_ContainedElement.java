




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class testModel_ContainedElement  {

    private String DoubleObj;
    private String Character;
    private float double;
    private String char;
    private String byteObject;
    private LocalDate date;
    private float float;
    private String DiagnosticChain;
    private String elementType;
    private String byteArray;
    private String name;





    private testModel_Kategorie testmodel_kategorie;


    public testModel_ContainedElement(
        String DoubleObj,        String Character,        float double,        String char,        String byteObject,        LocalDate date,        float float,        String DiagnosticChain,        String elementType,        String byteArray,        String name    ) {
        this.DoubleObj = DoubleObj;
        this.Character = Character;
        this.double = double;
        this.char = char;
        this.byteObject = byteObject;
        this.date = date;
        this.float = float;
        this.DiagnosticChain = DiagnosticChain;
        this.elementType = elementType;
        this.byteArray = byteArray;
        this.name = name;
    }


    public String getDoubleobj() {
        return DoubleObj;
    }

    public void setDoubleobj(String DoubleObj) {
        this.DoubleObj = DoubleObj;
    }
    public String getCharacter() {
        return Character;
    }

    public void setCharacter(String Character) {
        this.Character = Character;
    }
    public float getDouble() {
        return double;
    }

    public void setDouble(float double) {
        this.double = double;
    }
    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
    }
    public String getByteobject() {
        return byteObject;
    }

    public void setByteobject(String byteObject) {
        this.byteObject = byteObject;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public float getFloat() {
        return float;
    }

    public void setFloat(float float) {
        this.float = float;
    }
    public String getDiagnosticchain() {
        return DiagnosticChain;
    }

    public void setDiagnosticchain(String DiagnosticChain) {
        this.DiagnosticChain = DiagnosticChain;
    }
    public String getElementtype() {
        return elementType;
    }

    public void setElementtype(String elementType) {
        this.elementType = elementType;
    }
    public String getBytearray() {
        return byteArray;
    }

    public void setBytearray(String byteArray) {
        this.byteArray = byteArray;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public testModel_Kategorie getTestmodel_kategorie() {
        return testmodel_kategorie;
    }

    public void setTestmodel_kategorie(testModel_Kategorie testmodel_kategorie) {
        this.testmodel_kategorie = testmodel_kategorie;
    }

}