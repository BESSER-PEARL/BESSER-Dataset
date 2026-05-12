





import java.util.List;
import java.util.ArrayList;

public class File  {

    private None file_type;





    private User user;




    private Data data;


    public File(
        None file_type    ) {
        this.file_type = file_type;
    }


    public None getFile_type() {
        return file_type;
    }

    public void setFile_type(None file_type) {
        this.file_type = file_type;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public Data getData() {
        return data;
    }

    public void setData(Data data) {
        this.data = data;
    }

}