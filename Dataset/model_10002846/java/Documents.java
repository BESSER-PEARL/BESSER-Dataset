





import java.util.List;
import java.util.ArrayList;

public class Documents  {

    private None data;
    private int tab_counter;
    private String file_name;
    private String file;



    public Documents(
        None data,        int tab_counter,        String file_name,        String file    ) {
        this.data = data;
        this.tab_counter = tab_counter;
        this.file_name = file_name;
        this.file = file;
    }


    public None getData() {
        return data;
    }

    public void setData(None data) {
        this.data = data;
    }
    public int getTab_counter() {
        return tab_counter;
    }

    public void setTab_counter(int tab_counter) {
        this.tab_counter = tab_counter;
    }
    public String getFile_name() {
        return file_name;
    }

    public void setFile_name(String file_name) {
        this.file_name = file_name;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }


}