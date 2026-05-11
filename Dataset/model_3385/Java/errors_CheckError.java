





import java.util.List;
import java.util.ArrayList;

public class errors_CheckError extends Error {

    private String nameTable;
    private String porcent;
    private String nameCk;





    private List<errors_ColumnCk> errors_columncks;


    public errors_CheckError(
        String nameTable,        String porcent,        String nameCk    ) {
        super(
        );
        this.nameTable = nameTable;
        this.porcent = porcent;
        this.nameCk = nameCk;
        this.errors_columncks = new ArrayList<>();
    }

    public errors_CheckError(
        String nameTable,        String porcent,        String nameCk        ArrayList<errors_ColumnCk> errors_columncks    ) {
        this.nameTable = nameTable;
        this.porcent = porcent;
        this.nameCk = nameCk;
        this.errors_columncks = errors_columncks;
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
    public String getNameck() {
        return nameCk;
    }

    public void setNameck(String nameCk) {
        this.nameCk = nameCk;
    }

    public List<errors_ColumnCk> getErrors_columncks() {
        return errors_columncks;
    }

    public void addErrors_columnck(Errors_columnck errors_columnck) {
        this.errors_columncks.add(errors_columnck);
    }

}