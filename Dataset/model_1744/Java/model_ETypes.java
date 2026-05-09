




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_ETypes  {

    private String eChar;
    private String eBigDecimal;
    private float eDouble;
    private int eInt;
    private String uris;
    private String eByteArray;
    private float eFloat;
    private boolean eBoolean;
    private String eBigInteger;
    private String eString;
    private String eShort;
    private LocalDate eDate;
    private String eLong;
    private String eByte;



    public model_ETypes(
        String eChar,        String eBigDecimal,        float eDouble,        int eInt,        String uris,        String eByteArray,        float eFloat,        boolean eBoolean,        String eBigInteger,        String eString,        String eShort,        LocalDate eDate,        String eLong,        String eByte    ) {
        this.eChar = eChar;
        this.eBigDecimal = eBigDecimal;
        this.eDouble = eDouble;
        this.eInt = eInt;
        this.uris = uris;
        this.eByteArray = eByteArray;
        this.eFloat = eFloat;
        this.eBoolean = eBoolean;
        this.eBigInteger = eBigInteger;
        this.eString = eString;
        this.eShort = eShort;
        this.eDate = eDate;
        this.eLong = eLong;
        this.eByte = eByte;
    }


    public String getEchar() {
        return eChar;
    }

    public void setEchar(String eChar) {
        this.eChar = eChar;
    }
    public String getEbigdecimal() {
        return eBigDecimal;
    }

    public void setEbigdecimal(String eBigDecimal) {
        this.eBigDecimal = eBigDecimal;
    }
    public float getEdouble() {
        return eDouble;
    }

    public void setEdouble(float eDouble) {
        this.eDouble = eDouble;
    }
    public int getEint() {
        return eInt;
    }

    public void setEint(int eInt) {
        this.eInt = eInt;
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
    public float getEfloat() {
        return eFloat;
    }

    public void setEfloat(float eFloat) {
        this.eFloat = eFloat;
    }
    public boolean getEboolean() {
        return eBoolean;
    }

    public void setEboolean(boolean eBoolean) {
        this.eBoolean = eBoolean;
    }
    public String getEbiginteger() {
        return eBigInteger;
    }

    public void setEbiginteger(String eBigInteger) {
        this.eBigInteger = eBigInteger;
    }
    public String getEstring() {
        return eString;
    }

    public void setEstring(String eString) {
        this.eString = eString;
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
    public String getElong() {
        return eLong;
    }

    public void setElong(String eLong) {
        this.eLong = eLong;
    }
    public String getEbyte() {
        return eByte;
    }

    public void setEbyte(String eByte) {
        this.eByte = eByte;
    }


}