




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class testModel_ContainedLeaf  {

    private String name;
    private String elementType;
    private float double;
    private String Character;
    private String byteArray;
    private LocalDate date;
    private String char;
    private String byteObject;
    private float float;
    private String DoubleObj;



    public testModel_ContainedLeaf(
        String name,        String elementType,        float double,        String Character,        String byteArray,        LocalDate date,        String char,        String byteObject,        float float,        String DoubleObj    ) {
        this.name = name;
        this.elementType = elementType;
        this.double = double;
        this.Character = Character;
        this.byteArray = byteArray;
        this.date = date;
        this.char = char;
        this.byteObject = byteObject;
        this.float = float;
        this.DoubleObj = DoubleObj;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getElementtype() {
        return elementType;
    }

    public void setElementtype(String elementType) {
        this.elementType = elementType;
    }
    public float getDouble() {
        return double;
    }

    public void setDouble(float double) {
        this.double = double;
    }
    public String getCharacter() {
        return Character;
    }

    public void setCharacter(String Character) {
        this.Character = Character;
    }
    public String getBytearray() {
        return byteArray;
    }

    public void setBytearray(String byteArray) {
        this.byteArray = byteArray;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
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
    public float getFloat() {
        return float;
    }

    public void setFloat(float float) {
        this.float = float;
    }
    public String getDoubleobj() {
        return DoubleObj;
    }

    public void setDoubleobj(String DoubleObj) {
        this.DoubleObj = DoubleObj;
    }


}