





import java.util.List;
import java.util.ArrayList;

public class ric_Datepicker extends TextField, RichWidget {

    private boolean showWeekOfYear;
    private int numberMonthsToShow;
    private String locale;
    private boolean showButtonImage;
    private String dateFormat;
    private boolean showMonthMenu;
    private boolean showButtonClosePanel;
    private boolean showYearMenu;



    public ric_Datepicker(
        boolean showWeekOfYear,        int numberMonthsToShow,        String locale,        boolean showButtonImage,        String dateFormat,        boolean showMonthMenu,        boolean showButtonClosePanel,        boolean showYearMenu    ) {
        super(
        );
        this.showWeekOfYear = showWeekOfYear;
        this.numberMonthsToShow = numberMonthsToShow;
        this.locale = locale;
        this.showButtonImage = showButtonImage;
        this.dateFormat = dateFormat;
        this.showMonthMenu = showMonthMenu;
        this.showButtonClosePanel = showButtonClosePanel;
        this.showYearMenu = showYearMenu;
    }


    public boolean getShowweekofyear() {
        return showWeekOfYear;
    }

    public void setShowweekofyear(boolean showWeekOfYear) {
        this.showWeekOfYear = showWeekOfYear;
    }
    public int getNumbermonthstoshow() {
        return numberMonthsToShow;
    }

    public void setNumbermonthstoshow(int numberMonthsToShow) {
        this.numberMonthsToShow = numberMonthsToShow;
    }
    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
    }
    public boolean getShowbuttonimage() {
        return showButtonImage;
    }

    public void setShowbuttonimage(boolean showButtonImage) {
        this.showButtonImage = showButtonImage;
    }
    public String getDateformat() {
        return dateFormat;
    }

    public void setDateformat(String dateFormat) {
        this.dateFormat = dateFormat;
    }
    public boolean getShowmonthmenu() {
        return showMonthMenu;
    }

    public void setShowmonthmenu(boolean showMonthMenu) {
        this.showMonthMenu = showMonthMenu;
    }
    public boolean getShowbuttonclosepanel() {
        return showButtonClosePanel;
    }

    public void setShowbuttonclosepanel(boolean showButtonClosePanel) {
        this.showButtonClosePanel = showButtonClosePanel;
    }
    public boolean getShowyearmenu() {
        return showYearMenu;
    }

    public void setShowyearmenu(boolean showYearMenu) {
        this.showYearMenu = showYearMenu;
    }


}