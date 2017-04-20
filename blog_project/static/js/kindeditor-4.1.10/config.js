KindEditor.ready(function(K) {
               K.create('textarea[name=content]', {
					width: '1000px',
					height: '500px',
					uploadJson: '/admin/upload/kindeditor',
			   });
			   K.create('textarea[name=desc]', {
                    width: '1000px',
                    height: '100px',
                    uploadJson: '/admin/upload/kindeditor',
               });
        });
