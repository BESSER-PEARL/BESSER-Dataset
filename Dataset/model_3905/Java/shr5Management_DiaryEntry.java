





import java.util.List;
import java.util.ArrayList;

public class shr5Management_DiaryEntry  {

    private String date;
    private String message;





    private shr5Management_CharacterDiary shr5management_characterdiary;


    public shr5Management_DiaryEntry(
        String date,        String message    ) {
        this.date = date;
        this.message = message;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public shr5Management_CharacterDiary getShr5management_characterdiary() {
        return shr5management_characterdiary;
    }

    public void setShr5management_characterdiary(shr5Management_CharacterDiary shr5management_characterdiary) {
        this.shr5management_characterdiary = shr5management_characterdiary;
    }

}