





import java.util.List;
import java.util.ArrayList;

public class ric_Datepicker extends RichWidget, TextField {

    private boolean showWeekOfYear;
    private boolean showMonthMenu;
    private String locale;
    private int numberMonthsToShow;
    private boolean showButtonImage;
    private boolean showButtonClosePanel;
    private boolean showYearMenu;
    private String dateFormat;



    public ric_Datepicker(
        boolean showWeekOfYear,        boolean showMonthMenu,        String locale,        int numberMonthsToShow,        boolean showButtonImage,        boolean showButtonClosePanel,        boolean showYearMenu,        String dateFormat    ) {
        super(
        );
        this.showWeekOfYear = showWeekOfYear;
        this.showMonthMenu = showMonthMenu;
        this.locale = locale;
        this.numberMonthsToShow = numberMonthsToShow;
        this.showButtonImage = showButtonImage;
        this.showButtonClosePanel = showButtonClosePanel;
        this.showYearMenu = showYearMenu;
        this.dateFormat = dateFormat;
    }


    public boolean getShowweekofyear() {
        return showWeekOfYear;
    }

    public void setShowweekofyear(boolean showWeekOfYear) {
        this.showWeekOfYear = showWeekOfYear;
    }
    public boolean getShowmonthmenu() {
        return showMonthMenu;
    }

    public void setShowmonthmenu(boolean showMonthMenu) {
        this.showMonthMenu = showMonthMenu;
    }
    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
    }
    public int getNumbermonthstoshow() {
        return numberMonthsToShow;
    }

    public void setNumbermonthstoshow(int numberMonthsToShow) {
        this.numberMonthsToShow = numberMonthsToShow;
    }
    public boolean getShowbuttonimage() {
        return showButtonImage;
    }

    public void setShowbuttonimage(boolean showButtonImage) {
        this.showButtonImage = showButtonImage;
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
    public String getDateformat() {
        return dateFormat;
    }

    public void setDateformat(String dateFormat) {
        this.dateFormat = dateFormat;
    }


}