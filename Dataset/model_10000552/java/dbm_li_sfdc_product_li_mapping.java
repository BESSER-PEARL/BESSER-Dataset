





import java.util.List;
import java.util.ArrayList;

public class dbm_li_sfdc_product_li_mapping  {

    private String sfdc_product_id;
    private String dub_allocation_label;
    private String dbm_line_item_id;
    private String dbm_io_id;
    private String dbm_creative_ids;



    public dbm_li_sfdc_product_li_mapping(
        String sfdc_product_id,        String dub_allocation_label,        String dbm_line_item_id,        String dbm_io_id,        String dbm_creative_ids    ) {
        this.sfdc_product_id = sfdc_product_id;
        this.dub_allocation_label = dub_allocation_label;
        this.dbm_line_item_id = dbm_line_item_id;
        this.dbm_io_id = dbm_io_id;
        this.dbm_creative_ids = dbm_creative_ids;
    }


    public String getSfdc_product_id() {
        return sfdc_product_id;
    }

    public void setSfdc_product_id(String sfdc_product_id) {
        this.sfdc_product_id = sfdc_product_id;
    }
    public String getDub_allocation_label() {
        return dub_allocation_label;
    }

    public void setDub_allocation_label(String dub_allocation_label) {
        this.dub_allocation_label = dub_allocation_label;
    }
    public String getDbm_line_item_id() {
        return dbm_line_item_id;
    }

    public void setDbm_line_item_id(String dbm_line_item_id) {
        this.dbm_line_item_id = dbm_line_item_id;
    }
    public String getDbm_io_id() {
        return dbm_io_id;
    }

    public void setDbm_io_id(String dbm_io_id) {
        this.dbm_io_id = dbm_io_id;
    }
    public String getDbm_creative_ids() {
        return dbm_creative_ids;
    }

    public void setDbm_creative_ids(String dbm_creative_ids) {
        this.dbm_creative_ids = dbm_creative_ids;
    }


}