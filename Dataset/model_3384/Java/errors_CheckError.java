





import java.util.List;
import java.util.ArrayList;

public class errors_CheckError extends Error {

    private String nameCk;
    private String nameTable;
    private String porcent;



    public errors_CheckError(
        String nameCk,        String nameTable,        String porcent    ) {
        super(
        );
        this.nameCk = nameCk;
        this.nameTable = nameTable;
        this.porcent = porcent;
    }


    public String getNameck() {
        return nameCk;
    }

    public void setNameck(String nameCk) {
        this.nameCk = nameCk;
    }
    public String getNametable() {
        return nameTable;
    }

    public void setNametable(String nameTable) {
        this.nameTable = nameTable;
    }
    public String getPorcent() {
        return porcent;
    }

    public void setPorcent(String porcent) {
        this.porcent = porcent;
    }


}