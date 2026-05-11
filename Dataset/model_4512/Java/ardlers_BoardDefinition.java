





import java.util.List;
import java.util.ArrayList;

public class ardlers_BoardDefinition  {

    private int di;
    private int ain;
    private int aout;
    private String name;
    private int do;





    private ardlers_Library ardlers_library;


    public ardlers_BoardDefinition(
        int di,        int ain,        int aout,        String name,        int do    ) {
        this.di = di;
        this.ain = ain;
        this.aout = aout;
        this.name = name;
        this.do = do;
    }


    public int getDi() {
        return di;
    }

    public void setDi(int di) {
        this.di = di;
    }
    public int getAin() {
        return ain;
    }

    public void setAin(int ain) {
        this.ain = ain;
    }
    public int getAout() {
        return aout;
    }

    public void setAout(int aout) {
        this.aout = aout;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getDo() {
        return do;
    }

    public void setDo(int do) {
        this.do = do;
    }

    public ardlers_Library getArdlers_library() {
        return ardlers_library;
    }

    public void setArdlers_library(ardlers_Library ardlers_library) {
        this.ardlers_library = ardlers_library;
    }

}