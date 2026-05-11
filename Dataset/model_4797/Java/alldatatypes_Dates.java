




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class alldatatypes_Dates extends Type {

    private LocalDate dates;
    private LocalDate date_01_HMSms;
    private LocalDate date_01_HMS;
    private LocalDate dateEmptyDefault_01;
    private LocalDate date_01_HM;
    private LocalDate notEditableDate_01;
    private LocalDate date_1;
    private LocalDate date_01;



    public alldatatypes_Dates(
        LocalDate dates,        LocalDate date_01_HMSms,        LocalDate date_01_HMS,        LocalDate dateEmptyDefault_01,        LocalDate date_01_HM,        LocalDate notEditableDate_01,        LocalDate date_1,        LocalDate date_01    ) {
        super(
        );
        this.dates = dates;
        this.date_01_HMSms = date_01_HMSms;
        this.date_01_HMS = date_01_HMS;
        this.dateEmptyDefault_01 = dateEmptyDefault_01;
        this.date_01_HM = date_01_HM;
        this.notEditableDate_01 = notEditableDate_01;
        this.date_1 = date_1;
        this.date_01 = date_01;
    }


    public LocalDate getDates() {
        return dates;
    }

    public void setDates(LocalDate dates) {
        this.dates = dates;
    }
    public LocalDate getDate_01_hmsms() {
        return date_01_HMSms;
    }

    public void setDate_01_hmsms(LocalDate date_01_HMSms) {
        this.date_01_HMSms = date_01_HMSms;
    }
    public LocalDate getDate_01_hms() {
        return date_01_HMS;
    }

    public void setDate_01_hms(LocalDate date_01_HMS) {
        this.date_01_HMS = date_01_HMS;
    }
    public LocalDate getDateemptydefault_01() {
        return dateEmptyDefault_01;
    }

    public void setDateemptydefault_01(LocalDate dateEmptyDefault_01) {
        this.dateEmptyDefault_01 = dateEmptyDefault_01;
    }
    public LocalDate getDate_01_hm() {
        return date_01_HM;
    }

    public void setDate_01_hm(LocalDate date_01_HM) {
        this.date_01_HM = date_01_HM;
    }
    public LocalDate getNoteditabledate_01() {
        return notEditableDate_01;
    }

    public void setNoteditabledate_01(LocalDate notEditableDate_01) {
        this.notEditableDate_01 = notEditableDate_01;
    }
    public LocalDate getDate_1() {
        return date_1;
    }

    public void setDate_1(LocalDate date_1) {
        this.date_1 = date_1;
    }
    public LocalDate getDate_01() {
        return date_01;
    }

    public void setDate_01(LocalDate date_01) {
        this.date_01 = date_01;
    }


}