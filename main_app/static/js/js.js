 $(document).ready(function () {
        $('#inputSearch').on('input', function () {
            let searchvalue = $(this).val();
            let csrfToken = $('[name=csrfmiddlewaretoken]').val();
            
            let urls=""
            let table=$(this).attr('name')
            if (table=='searchbook'){
                 urls = $(this).data('searchbook-url');
            }
            if(table=='searchmember'){
               urls = $(this).data('searchmember-url');
            }
            if (searchvalue !== "") {
                $.post(urls, 
                    {
                        q: searchvalue,
                        csrfmiddlewaretoken: csrfToken
                    },
                    function (data, status) {
                        alert(status)
                        $("table").html(data);
                    });
            }
             else {
                window.location.reload() // Reload the page if input is empty
            }
        });
    });