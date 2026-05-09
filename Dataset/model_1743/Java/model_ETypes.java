




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_ETypes  {

    private float eFloat;
    private String eByteArray;
    private String eString;
    private float eDouble;
    private String eChar;
    private LocalDate eDate;
    private String eByte;
    private String uris;
    private String eBigInteger;
    private String eShort;
    private boolean eBoolean;
    private String eBigDecimal;
    private int eInt;
    private String eLong;



    public model_ETypes(
        float eFloat,        String eByteArray,        String eString,        float eDouble,        String eChar,        LocalDate eDate,        String eByte,        String uris,        String eBigInteger,        String eShort,        boolean eBoolean,        String eBigDecimal,        int eInt,        String eLong    ) {
        this.eFloat = eFloat;
        this.eByteArray = eByteArray;
        this.eString = eString;
        this.eDouble = eDouble;
        this.eChar = eChar;
        this.eDate = eDate;
        this.eByte = eByte;
        this.uris = uris;
        this.eBigInteger = eBigInteger;
        this.eShort = eShort;
        this.eBoolean = eBoolean;
        this.eBigDecimal = eBigDecimal;
        this.eInt = eInt;
        this.eLong = eLong;
    }


    public float getEfloat() {
        return eFloat;
    }

    public void setEfloat(float eFloat) {
        this.eFloat = eFloat;
    }
    public String getEbytearray() {
        return eByteArray;
    }

    public void setEbytearray(String eByteArray) {
        this.eByteArray = eByteArray;
    }
    public String getEstring() {
        return eString;
    }

    public void setEstring(String eString) {
        this.eString = eString;
    }
    public float getEdouble() {
        return eDouble;
    }

    public void setEdouble(float eDouble) {
        this.eDouble = eDouble;
    }
    public String getEchar() {
        return eChar;
    }

    public void setEchar(String eChar) {
        this.eChar = eChar;
    }
    public LocalDate getEdate() {
        return eDate;
    }

    public void setEdate(LocalDate eDate) {
        this.eDate = eDate;
    }
    public String getEbyte() {
        return eByte;
    }

    public void setEbyte(String eByte) {
        this.eByte = eByte;
    }
    public String getUris() {
        return uris;
    }

    public void setUris(String uris) {
        this.uris = uris;
    }
    public String getEbiginteger() {
        return eBigInteger;
    }

    public void setEbiginteger(String eBigInteger) {
        this.eBigInteger = eBigInteger;
    }
    public String getEshort() {
        return eShort;
    }

    public void setEshort(String eShort) {
        this.eShort = eShort;
    }
    public boolean getEboolean() {
        return eBoolean;
    }

    public void setEboolean(boolean eBoolean) {
        this.eBoolean = eBoolean;
    }
    public String getEbigdecimal() {
        return eBigDecimal;
    }

    public void setEbigdecimal(String eBigDecimal) {
        this.eBigDecimal = eBigDecimal;
    }
    public int getEint() {
        return eInt;
    }

    public void setEint(int eInt) {
        this.eInt = eInt;
    }
    public String getElong() {
        return eLong;
    }

    public void setElong(String eLong) {
        this.eLong = eLong;
    }


}