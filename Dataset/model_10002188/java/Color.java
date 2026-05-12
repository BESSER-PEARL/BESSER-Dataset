





import java.util.List;
import java.util.ArrayList;

public class Color  {

    private String ColorName;
    private String ColorID;



    public Color(
        String ColorName,        String ColorID    ) {
        this.ColorName = ColorName;
        this.ColorID = ColorID;
    }


    public String getColorname() {
        return ColorName;
    }

    public void setColorname(String ColorName) {
        this.ColorName = ColorName;
    }
    public String getColorid() {
        return ColorID;
    }

    public void setColorid(String ColorID) {
        this.ColorID = ColorID;
    }


}