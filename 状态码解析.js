
fetch(
  "http://career.huawei.com/reccampportal/services/portal/portaluser/queryMyJobInterviewEvolve?reqTim=" +
    new Date().getTime()
)
  .then(res => res.json())
  .then(data => {
    var n = null;
    var i = new JSEncrypt();
    i.setPrivateKey(
      "MaUbwt6RJSJLY104JM6eifoyEZ5FpNA1HMWbz7n12yL6Ycqbg33kKw33ZoZHcUyDWUnO/FLNy1x4FQ5IDk0iorNam7jDG9xa/bVKXSswn356g9i9B8FaHxYLWEGrTTR4C7hQor5f5E/DHqp/SOo/oD3nRUbGz1DFSYdLG2f0TqkLTyg4xo3ceTjRCc6R0e6O4VWL0EN3wAUnMC+tX0SUoJb7AUE/eESOgexGVbIxYgl5mTGreApKIp1rDuM0JrIoVXRQM7ZIo9ut0CvKC9UsmN8+8Sw1WpaVpL26AdPwkVQ9dy4kWiXlPbCPAhr+E6BtvX1hS8FtSinkXBt7PIfIDzVDvqPBd8qkeUH6gnJimjRKGIGV3Qv1f1DaS7fdUYwsMEOSTfpmb2xPaaQiH9lQlRTV3VkJ99TpWN50mAug+nACOBy+SWHTEQd0omt/yMoTpH+nQbY/8lRPHcTbmSUQsA/tQP2C0ZT6iwtCGY6uoDFVIo3YPwPc9Bc71HW6oY9WABpGHAoOUVfBKcufn5g/Hkp9JqXHvhkTHbgQvBPkrUfWxKIATiCpNn40VPnXJ0jZUivl16oFa2UlFpXawTjiS/Rg9/xtzQ/fTQrW4gBjK4Sw0FmF4q9zteAtVDT4qAXbdu7zRiZdvJolbiS1rQsaq/62ZMwvhfhv6pzTwsqRgt0EH2WAfQ9Xc5aP97jstXQ1MNs+wNT0dOPd379Zy+hLut7E176BzVtYouVFnEbjHN32BQqFwG7OowFswhpaMUaKI1aeezTzxhD/l5xZR+TcnY1PFkRiuQD/a6ydh5hWfRnnHGlsX2pdaXssJbEc3MGiXUpBPoWr7t1e364t6kg4RWat+yXPuj/dppFm6l39pGQcgm+wDp+HXNxS7StSlmOORMDrRBk4WEW3Ptkvh2xEUClaoN8K8tcQbXuiRuaVGH5EHG603mcSROQ39+tgSLLQNeLJ0W9KrxFv3+hdLraBiJPVCE7JdAqXZA/FJjng9v0lf2UvVsEcjnwpKwEo9AtcACbQs8E7fodiAVuAh7ATVNIsH/D/eobKFeSNbPiu//iMNb1zK2aHQM0Wqy2b3cLn+bmHWFR/Q7NlTZEA6YdW3czFWpEt5P/Kii1eZXzGc4Fks2N6jJTeQUgKtdzvUra5jTvikHAW13mpLgQvnBGRPsMKsiBmxJszpGbQ6WDkxGxA0ywAtnrVywwtDM9YI9APofFz1zsq2/Hd1DTRDlm/8jklVD8gvc5D+USg9PgOxB0QcjiIAld2rRjwX5xet7fJhEVxllI3jvNm2V2dL0iOLknkGFVs8kNUJj3lxAcJRUeUjkuAoXKe2VL/Mmtk4o/eu+j9tsMtN76gvDWxCPnu/FkbseZ/+4r/wqSCEidrxp69kvuXA/Kuy1CS9oUICfIej7VHsPWGUUEkLBINAZE19y/xHrD/19ZnNXWO3e+ItIawL51kJsFHGzuJ9UhxDps5ROoRXeerH8S1WZhW14X2wSh5Y+iu3KmLi6Mahhwr5r+RbWy7uO8fFa7eSPslOuxQ"
    ),
      (n = i.decryptLong2(data.cipherText)) &&
        (n = JSON.parse(decodeURIComponent(n)));
    console.log(JSON.stringify(n, 0, 4));
  });
 