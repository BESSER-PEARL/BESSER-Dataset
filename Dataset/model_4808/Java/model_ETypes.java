




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_ETypes  {

    private String eLong;
    private String eShort;
    private LocalDate eDate;
    private String eStrings;
    private int eInts;
    private String eBooleans;
    private float eDouble;
    private boolean eBoolean;
    private int eInt;
    private String eString;
    private String uris;
    private String eByteArray;
    private String doubleValue;
    private String eChar;
    private String eDoubles;
    private String eByte;
    private float eFloat;



    public model_ETypes(
        String eLong,        String eShort,        LocalDate eDate,        String eStrings,        int eInts,        String eBooleans,        float eDouble,        boolean eBoolean,        int eInt,        String eString,        String uris,        String eByteArray,        String doubleValue,        String eChar,        String eDoubles,        String eByte,        float eFloat    ) {
        this.eLong = eLong;
        this.eShort = eShort;
        this.eDate = eDate;
        this.eStrings = eStrings;
        this.eInts = eInts;
        this.eBooleans = eBooleans;
        this.eDouble = eDouble;
        this.eBoolean = eBoolean;
        this.eInt = eInt;
        this.eString = eString;
        this.uris = uris;
        this.eByteArray = eByteArray;
        this.doubleValue = doubleValue;
        this.eChar = eChar;
        this.eDoubles = eDoubles;
        this.eByte = eByte;
        this.eFloat = eFloat;
    }


    public String getElong() {
        return eLong;
    }

    public void setElong(String eLong) {
        this.eLong = eLong;
    }
    public String getEshort() {
        return eShort;
    }

    public void setEshort(String eShort) {
        this.eShort = eShort;
    }
    public LocalDate getEdate() {
        return eDate;
    }

    public void setEdate(LocalDate eDate) {
        this.eDate = eDate;
    }
    public String getEstrings() {
        return eStrings;
    }

    public void setEstrings(String eStrings) {
        this.eStrings = eStrings;
    }
    public int getEints() {
        return eInts;
    }

    public void setEints(int eInts) {
        this.eInts = eInts;
    }
    public String getEbooleans() {
        return eBooleans;
    }

    public void setEbooleans(String eBooleans) {
        this.eBooleans = eBooleans;
    }
    public float getEdouble() {
        return eDouble;
    }

    public void setEdouble(float eDouble) {
        this.eDouble = eDouble;
    }
    public boolean getEboolean() {
        return eBoolean;
    }

    public void setEboolean(boolean eBoolean) {
        this.eBoolean = eBoolean;
    }
    public int getEint() {
        return eInt;
    }

    public void setEint(int eInt) {
        this.eInt = eInt;
    }
    public String getEstring() {
        return eString;
    }

    public void setEstring(String eString) {
        this.eString = eString;
    }
    public String getUris() {
        return uris;
    }

    public void setUris(String uris) {
        this.uris = uris;
    }
    public String getEbytearray() {
        return eByteArray;
    }

    public void setEbytearray(String eByteArray) {
        this.eByteArray = eByteArray;
    }
    public String getDoublevalue() {
        return doubleValue;
    }

    public void setDoublevalue(String doubleValue) {
        this.doubleValue = doubleValue;
    }
    public String getEchar() {
        return eChar;
    }

    public void setEchar(String eChar) {
        this.eChar = eChar;
    }
    public String getEdoubles() {
        return eDoubles;
    }

    public void setEdoubles(String eDoubles) {
        this.eDoubles = eDoubles;
    }
    public String getEbyte() {
        return eByte;
    }

    public void setEbyte(String eByte) {
        this.eByte = eByte;
    }
    public float getEfloat() {
        return eFloat;
    }

    public void setEfloat(float eFloat) {
        this.eFloat = eFloat;
    }


}