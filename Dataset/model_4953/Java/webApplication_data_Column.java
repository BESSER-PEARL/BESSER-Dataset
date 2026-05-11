





import java.util.List;
import java.util.ArrayList;

public class webApplication_data_Column extends Named {

    private String type;
    private boolean PK;
    private int lenght;



    public webApplication_data_Column(
        String type,        boolean PK,        int lenght    ) {
        super(
        );
        this.type = type;
        this.PK = PK;
        this.lenght = lenght;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getPk() {
        return PK;
    }

    public void setPk(boolean PK) {
        this.PK = PK;
    }
    public int getLenght() {
        return lenght;
    }

    public void setLenght(int lenght) {
        this.lenght = lenght;
    }


}